from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from quizzer import quizActions, quizUtility
from account.models import UserProfile
from lessons.models import Lesson,Level
from englishgrammar.models import EnglishVerb
from django.core.paginator import Paginator
from decimal import *
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User
from webpages.forms import SignUpForm

def home(request):
    if request.user.is_authenticated():
        return showLearningPage(request,request.user.profile.level)
    else:
        return showLearningPage(request,'1.00')
        
def signin(request):
    #authentication achieved. we're signed in. what now?
    if endOfCourse(request):
        return showEndOfCourse(request)
    else:
        return showLearningPage(request, request.user.profile.level)
        
def signout(request):
    logout(request)
    return redirect('webpages.views.home')

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
    #Make them level
    user_profile = user.profile
    user_profile.level = 1
    #they now know amo
    user_profile.known_verbs.add(EnglishVerb.objects.get(present='love'))
    user_profile.save()
    #finally, level them to 2
    levelUpPlayer(user_profile)

def is_attempted_login(request):
    if request.POST and 'login-email' in request.POST:
        return True
    else:
        return False

def sign_in_user(request):
    #Right now, all users have the password hello.
    user = authenticate(username=request.POST['login-email'], password='hello')
    if user is not None:
        login(request, user)
        return HttpResponseRedirect('/signin')
    

def showLearningPage(request, pageLevelString):
    
    #check such a page is in the course.
    if endOfCourse(request):
        return showEndOfCourse(request)
    
    #Attempted sign in.
    if is_attempted_login(request):
        return sign_in_user(request)
            
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
    
    #Sanity check - show course end if there.
    if endOfCourse(request):
        return render(request,'end-of-course.html',{})
    
    if is_attempted_login(request):
        return sign_in_user(request)
    
    if request.method == 'POST':
        #This isn't a sign-in attempt, as we'd have returned elsewhere from sign_in_user
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
                if levelUpIsPermissable(request):
                    #And we're allowed to level up!
                    levelUpPlayer(request.user.profile)
                    return showLearningPage(request, request.user.profile.level)
                else:
                    #Level up forbidden!
                    return showEndOfCourse(request)
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

def levelUpPlayer(user_profile):
    user_profile.level += 1
    for verb in Level.objects.get(level_number=user_profile.level).verb_unlocks.all():
        user_profile.known_verbs.add(verb)
    for noun in Level.objects.get(level_number=user_profile.level).noun_unlocks.all():
        user_profile.known_nouns.add(noun)
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
    
def endOfCourse(request):
    currentLevel = getCurrentLevel(request)
    try:
        possibleLevel = Level.objects.get(level_number=currentLevel.level_number)
    except:
        return True
    else:
        return False
    
def levelUpIsPermissable(request):
    currentLevel = getCurrentLevel(request).level_number
    nextLevel = str(int(currentLevel) + 1)
    try:
        intendedLevel = Level.objects.get(level_number=nextLevel)
    except:
        return False
    else:
        return True
    
def showEndOfCourse(request):
    return render(request,'end-of-course.html',{})