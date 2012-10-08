import random
from latingrammar import latinVerbs,latinNouns
from englishgrammar import englishVerbs, englishNouns
from sharedgrammar import utility
from quizzer import quizUtility
from latingrammar.models import *
from englishgrammar.models import *

def checkAnswer(correctAnswer,givenAnswer):
    #Returns [boolean,message]
    #message is html, escaped, so shouldn't contain original answer!
    if set( correctAnswer.split(" ")) == set(givenAnswer.split(" ") ):
        return (True,'<span style="color:green">Correct! Well done.</span>')
    else:
        #Answer is wrong.
        return [False,'<span style="color:red">Not quite. The answer was: <strong>' +correctAnswer+ '</strong>.</span>']

def getRandomVerb():
    englishVerb = quizUtility.generateVerb()
    latinVerb = englishVerb.translation
    person = random.randrange(1,7)
    
    question = getEnglishPronoun(person) + " " + englishVerbs.getEnglishVerbForm(englishVerb,person,'Present Active')
    answer = latinVerbs.getLatinVerbForm(latinVerb,person,'Present Active')
    return (question,answer)
    
def getEnglishPronoun(person):
    persons = (None, 'I', 'you', random.choice(['he','she']), 'we', 'you (pl.)', 'they')
    return persons[person]
    
def getRandomNoun():
    latinNoun = random.choice(LatinNoun.objects.all())
    return latinNouns.getLatinNounForm(latinNoun,'accusative','plural')

def getChapterThreeShortSentence():
    subjectPlurality = random.choice( ('singular','plural') )
    objectPlurality = random.choice( ('singular','plural') )
    person = utility.getPerson(3,subjectPlurality)
    
    words = quizUtility.getTriplet()
    
    #re-instate no duplication   
    
    question = ("The " + englishNouns.getEnglishNounForm(words[0],subjectPlurality) + " "
    + englishVerbs.getEnglishVerbForm(words[2],person,'Present Active') + " the " +
    englishNouns.getEnglishNounForm(words[1],objectPlurality) + "."
    )
    
    latinVerbModel = words[2].translation
    latinSubjectModel = words[0].translation
    latinObjectModel = words[1].translation
    
    answer = (latinNouns.getLatinNounForm(latinSubjectModel,'nominative',subjectPlurality) + " "
    + latinNouns.getLatinNounForm(latinObjectModel,'accusative',objectPlurality) + " " +
    latinVerbs.getLatinVerbForm(latinVerbModel,person,'Present Active')
    )
    
    return (question,answer)