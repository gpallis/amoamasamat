from django.http import HttpResponse
from django.shortcuts import render
from quizzer import quizActions
from account.models import UserProfile
from lessons.models import Lesson,Level
from django.core.paginator import Paginator
from decimal import *
from django.contrib.auth import login,authenticate

def home(request):
    return showLearningPage(request,'1.00')
    
def showLearningPage(request, pageLevelString):
    
    if request.POST and request.POST['email']:
        #Right now, all users have the password hello.
        user = authenticate(username=request.POST['email'], password='hello')
        if user is not None:
            login(request, user)
    
    #this is rather ugly - it could certainly be re-written, or more likely refactored w/ database changes ('course' model)
    #get the next/prev links, as appropriate
    
    pageLevel= float(pageLevelString)
    
    if Lesson.objects.filter(level=str(pageLevel+0.01)):
        next = str(pageLevel+0.01)
    else:
        next = False
        
    if Lesson.objects.filter(level=str(pageLevel-0.01)):
        prev = str(pageLevel-0.01)
    else:
        prev = False
    
    #in the long term, it might be dope to pass all the lessons, and javascript-iterate through them.        
    
    return render (request, 'showLesson.html', {
        'lesson':Lesson.objects.get(level=str(pageLevelString)),
        'next':next,
        'prev':prev,
        'user':request.user,
    })
    
def play(request):
    if request.method == 'POST':
        #Verdict returns [Boolean, feedback comment]
        verdict = quizActions.checkAnswer(request.session['correctAnswer'],request.POST['playerAnswer'])
        if verdict[0] == True:
            gainXP(request,verdict)
    else:
        verdict = [None,'']
    
    question = quizActions.getChapterThreeShortSentence()
    request.session['correctAnswer'] = question[1]
    
    progressBar = getProgress(request)
    
    return render(request,'showVerb.html',{
        'level':getCurrentLevel(request),
        'progress':progressBar,
        'question':question[0],
        'feedback':verdict[1],
        })

def getProgress(request):
    #returns percentile user progress
    if request.user.is_authenticated():
        #user's current xp, no problem
        xp = float(request.user.profile.xp)    
    else:
        #no logged-in user
        if ('xp') not in request.session:
            #if no xp for the session either, set it to 0.
            request.session['xp'] = 0
        #whether we just set it 0, or we're using an existing session['xp'], better make it a float
        xp = float(request.session['xp'])
        
    xpRequired = getCurrentLevel(request).number_of_questions
    
    return 100*(xp / xpRequired)
    
def getCurrentLevel(request):
    if request.user.is_authenticated():
        return Level.objects.get(level_number=request.user.profile.level)
    else:
        return Level.objects.get(level_number=1)

def gainXP(request,verdict):
    #player, (who may not be logged in), has just got an answer right.
    
    if request.user.is_authenticated():
        user_profile = request.user.profile
        user_profile.xp += 1
        user_profile.save()
        if checkForLevelUp(request):
            user_profile.level += 1
            user_profile.xp = 0
            user_profile.save()
    else:
        #player is not authenticated
        #there will always already be an xp parameter
        request.session['xp'] += 1
        request.session.save()
        
def checkForLevelUp(request):
    if request.user.is_authenticated():
        xp = request.user.profile.xp
    else:
        xp = request.session['xp']
        
    if xp >= getCurrentLevel(request).number_of_questions:
        return True
    else:
        return False