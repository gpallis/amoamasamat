from django.http import HttpResponse
from django.shortcuts import render, redirect
from quizzer import quizActions, quizUtility
from account.models import UserProfile
from lessons.models import Lesson,Level
from englishgrammar.models import EnglishVerb
from django.core.paginator import Paginator
from decimal import *
from django.contrib.auth import login,authenticate
from django.contrib.auth.models import User
from webpages.forms import SignUpForm

def home(request):
    return showLearningPage(request,'1.00')

def showSignUpPage(request):
    if request.POST and 'email' in request.POST: 
        #They've attempted to sign up!
        form = SignUpForm(request.POST)
        if not form.is_valid():
            #but with an invalid email.
            return render(request,'signup.html', {'error':'Invalid email address'})
            
        else:
            #form was valid
            #is the email in use?
            try:
                user = User.objects.get(email=form.cleaned_data['email'])
            except:
                #It's un-used!
                #so it's fine - create the account
                createAccount(form.cleaned_data['email'])
                
                #and sign 'em in
                signedInUser = authenticate(username=form.cleaned_data['email'],password='hello')
                login(request, signedInUser)
                #and finally, take em to the lesson!
                targetLesson = Lesson.objects.get(level='2.00')
                return redirect(targetLesson)
            else:
                #hang on, this email already exists!
                return render(request,'signup.html', {'error':'Email already in use'})
            
    
    else:
        #no form submitted, first-time viewing.
        return render(request,'signup.html', {})

def createAccount(email):
    user = User.objects.create_user(email,email,'hello')
    user.save()
    #Make them level 2
    user_profile = user.profile
    user_profile.level = 2
    #they now know amo
    user_profile.knownVerbs.add(EnglishVerb.objects.get(present='love'))
    user_profile.save()

def showLearningPage(request, pageLevelString):
    
    if request.POST and 'login-email' in request.POST:
        #Right now, all users have the password hello.
        user = authenticate(username=request.POST['login-email'], password='hello')
        if user is not None:
            login(request, user)
    
    #this is rather ugly - it could certainly be re-written, or more likely refactored w/ database changes
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
            #got the question right
            gainXP(request,verdict)
    else:
        #No post request made - we navigated to this page or were taken there by a link.
        verdict = [None,'']
        
    if checkForLevelUp(request):
            #We've just levelled up!
            if request.user.is_authenticated():
                #We're already logged in, so proceed as normal to a lesson.
                levelUpPlayer(request)
                return showLearningPage(request, request.user.profile.level)
            else:
                #But we're not logged in!
                return redirect('/signup/', request=request)
    
    else:
        #We haven't levelled up, so advance progress bars etc.
        #get the question
        question = quizUtility.getAppropriateQuestion(request)
        
        #set up the asking of it
        request.session['correctAnswer'] = question[1]
        
        progressBar = getProgress(request)
        
        return render(request,'showVerb.html',{
            'level':getCurrentLevel(request),
            'progress':progressBar,
            'question':question[0],
            'feedback':verdict[1],
            })

def levelUpPlayer(request):
    user_profile = request.user.profile
    user_profile.level += 1
    user_profile.xp = 0
    user_profile.save()
                

def getProgress(request):
    #returns percentile user progress
    if request.user.is_authenticated():
        #user's current xp, no problem
        xp = float(request.user.profile.xp)    
    else:
        #no logged-in user
        if ('xp') not in request.session:
            #if no xp for the session either, set it to 0.
            createSessionXP(request)
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
        
    else:
        #player is not authenticated
        #there will always already be an xp parameter
        request.session['xp'] += 1
        request.session.save()
        
def checkForLevelUp(request):
    if request.user.is_authenticated():
        xp = request.user.profile.xp
    else:
        if ('xp') not in request.session:
            createSessionXP(request)
        xp = request.session['xp']
        
    if xp >= getCurrentLevel(request).number_of_questions:
        return True
    else:
        return False
    
def createSessionXP(request):
    request.session['xp'] = 0
    