import random

#quizutility generates questions. Functionality like translation would be better in sharedgrammar.
from englishgrammar.models import *
from sharedgrammar.models import NounProperty
from lessons.models import Level
from django.contrib.auth.models import User
import quizActions

def getAppropriateQuestion(request):
    if request.user.is_authenticated():
        user_profile = request.user.profile
    else:
        user_profile = User.objects.get(username='.signed-out-user').profile
    
    levelObject = Level.objects.get(level_number=user_profile.level)
    generator = levelObject.question_generator
    generatorFunction = getGeneratorFunction(generator)
    return generatorFunction(user_profile)

def getGeneratorFunction(name):
    functionDictionary = {
        "threeWordSentence":quizActions.getChapterThreeShortSentence,
        "verb":quizActions.getRandomVerbQuestion
    }
    return functionDictionary[name]


def generateVerb(user_profile):
    return random.choice(user_profile.knownVerbs.all())

def getCompatibleNoun(verb,subjectOrObject, forbiddenWords = []):
    
    if subjectOrObject == 'subject':
        requirements = verb.subject_requires.all()
        exclusions = verb.subject_excludes.all()
    else:
        requirements = verb.object_requires.all()
        exclusions = verb.object_excludes.all()
        
    possibleNouns = EnglishNoun.objects.all()
    for desiredProperty in requirements:
        validNouns = desiredProperty.noun_set.all()
        possibleNouns = (possibleNouns & validNouns)
    
    for undesiredProperty in exclusions:
        invalidNouns = undesiredProperty.noun_set.all()
        possibleNouns = (possibleNouns - invalidNouns)
    
    chosenNoun = random.choice(possibleNouns)
    if chosenNoun in forbiddenWords:
        return getCompatibleNoun(verb, subjectOrObject,forbiddenWords)
    else:
        return chosenNoun
    
def getTriplet(user_profile):
    #returns a mutually compatible subject/object/verb set as a dictionary
    verb = generateVerb(user_profile)
    subject = getCompatibleNoun(verb,'subject')
    object = getCompatibleNoun(verb,'object', [subject])
    return (subject, object, verb)
    
    