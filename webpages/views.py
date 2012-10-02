from django.http import HttpResponse
from django.shortcuts import render
from quizzer import quizActions
from lessons.models import Lesson
from django.core.paginator import Paginator
from decimal import *
from django.contrib.auth import login,authenticate

def home(request):
    return showLearningPage(request, 0)
    
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
        previousAttemptResult = quizActions.checkAnswer(request.session['correctAnswer'],request.POST['playerAnswer'])[1]
    else:
        previousAttemptResult = ''
    
    question = quizActions.getChapterThreeShortSentence()
    request.session['correctAnswer'] = question[1]
    
    return render(request,'showVerb.html',{
        'question':question[0],
        'previousAttemptResult':previousAttemptResult,
        })
