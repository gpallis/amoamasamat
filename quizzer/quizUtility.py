import random

#quizutility generates questions. Functionality like translation would be better in sharedgrammar.
from englishgrammar.models import *
from sharedgrammar.models import NounProperty

def generateVerb(contraints):
    return random.choice(EnglishVerb.objects.all())

def getCompatibleNoun(verb,subjectOrObject):
    
    if subjectOrObject == 'subject':
        requirements = verb.subject_requires.all()
        exclusions = verb.subject_excludes.all()
    else:
        requirements = verb.object_requires.all()
        exclusions = verb.object_excludes.all()
        
    possibleNouns = EnglishNoun.objects.all()
    for desiredProperty in requirements:
        validNouns = desiredProperty.egg_set.all()
        possibleNouns = (possibleNouns & validNouns)
    
    for undesiredProperty in exclusions:
        invalidNouns = undesiredProperty.egg_set.all()
        possibleNouns = (possibleNouns - invalidNouns)
    
    return  random.choice(possibleNouns)
    
def getTriplet():
    #returns a mutually compatible subject/object/verb set as a dictionary
    verb = generateVerb(None)
    subject = getCompatibleNoun(verb,'subject')
    object = getCompatibleNoun(verb,'object')
    return (subject, object, verb)
    
    