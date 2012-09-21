from django.http import HttpResponse
from django.shortcuts import render
from quizzer import quizActions

def home(request):
    question = quizActions.askQuestion()
    return render(request,'showVerb.html',{
        'question':question[0],
        'answer':question[1]
        })
