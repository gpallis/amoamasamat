from django.http import HttpResponse
from django.shortcuts import render
from quizzer import quizActions
from webpages import whichPage

def home(request):
    playerLevel = 0
    return render (request, 'showLesson.html', {
        'lesson':whichPage.whichLesson(playerLevel),
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
