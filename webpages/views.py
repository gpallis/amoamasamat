from django.http import HttpResponse
from django.shortcuts import render
from quizzer import quizActions
from webpages import whichPage
from lessons.models import Lesson
from django.core.paginator import Paginator
from decimal import *
from django.contrib.auth import login,authenticate

def home(request):
    return showLearningPage(request, 0)
    
def showLearningPage(request, pageLevelString="0.01"):
    
    pageLevel= float(pageLevelString)
    #this is rather ugly - it could certainly be re-written, or more likely refactored w/ database changes ('course' model)
    if Lesson.objects.filter(level=str(pageLevel+0.01)):
        next = str(pageLevel+0.01)
    else:
        next = False
        
    if Lesson.objects.filter(level=str(pageLevel-0.01)):
        prev = str(pageLevel-0.01)
    else:
        prev = False
    
    #in the long term, it might be dope to pass all the lessons, and javascript-iterate through them.        
    whichPage.whichLesson(pageLevel)
    
    return render (request, 'showLesson.html', {
        'lesson':whichPage.whichLesson(pageLevelString),
        'next':next,
        'prev':prev,
        'user':request.user,
    })
    
def question(requestion):
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
