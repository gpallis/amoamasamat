import random
from latingrammar import actions
from englishgrammar import englishActions
from latingrammar.models import LatinVerb
from englishgrammar.models import EnglishVerb

def askQuestion():
    englishVerb = random.choice(EnglishVerb.objects.all())
    latinVerb = englishVerb.translation
    person = random.randrange(1,7)
    
    question = getEnglishPronoun(person) + " " + englishActions.getEnglishVerbForm(englishVerb,person,'Present Active')
    answer = actions.getLatinVerbForm(latinVerb,person,'Present Active')
    return (question,answer)
    
def getEnglishPronoun(person):
    persons = (None, 'I', 'you', random.choice(['he','she']), 'we', 'you (pl.)', 'they')
    return persons[person]