import random
from latingrammar import latinVerbs,latinNouns
from englishgrammar import englishVerbs
from latingrammar.models import *
from englishgrammar.models import *

def getRandomVerb():
    englishVerb = random.choice(EnglishVerb.objects.all())
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