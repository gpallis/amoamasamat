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
    if set( correctAnswer.lower().split(" ")) == set(givenAnswer.lower().split(" ") ):
        return (True,'<span style="color:green">Correct! Well done.</span>')
    else:
        #Answer is wrong.
        return [False,'<span style="color:red">Not quite. The answer was: <strong>' +correctAnswer+ '</strong>.</span>']

def getRandomVerbQuestion(user_profile):
    englishVerb = quizUtility.generateVerb(user_profile)
    latinVerb = englishVerb.translation
    person = random.randrange(1,7)
    
    question = getEnglishPronoun(person) + " " + englishVerbs.getEnglishVerbForm(englishVerb,person,'Present Active')
    answer = latinVerbs.getLatinVerbForm(latinVerb,person,'Present Active')
    return (question,answer)
    
def getEnglishPronoun(person):
    persons = (None, 'I', 'You', random.choice(['He','She','It']), 'We', 'You (plural)', 'They')
    return persons[person]

def getPreamble(case):
    if case == 'genitive':
        return "of the"
    if case == 'dative':
        return "to the"
    if case == 'ablative':
        return "by the"
    
    #None of these
    return ""
    
def getEnglishOneWordSentence(noun,plurality,case):
    return (getPreamble(case) + " " + englishNouns.getEnglishNounForm(noun,plurality))
    
def genitiveOrDative(user_profile):
    englishNoun = quizUtility.generateNoun(user_profile)
    latinNoun = englishNoun.translation
    
    case = random.choice(['genitive', 'dative'])
    plurality = random.choice(['singular','plural'])
    
    question = getEnglishOneWordSentence(englishNoun,plurality,case)
    answer = latinNouns.getLatinNounForm(latinNoun,case,plurality)
    return (question,answer)
    
def twoWordNominativeSentence(user_profile):
    englishVerb = quizUtility.generateVerb(user_profile)
    latinVerb = englishVerb.translation
    
    englishNoun = quizUtility.getCompatibleNoun(englishVerb,user_profile,'subject')
    latinNoun = englishNoun.translation
    
    subjectPlurality = random.choice( ('singular', 'plural') )
    verbPerson = 3
    if subjectPlurality == 'plural':
        verbPerson = 6
    
    question = ("The " + englishNouns.getEnglishNounForm(englishNoun,subjectPlurality)
                + " " + englishVerbs.getEnglishVerbForm(englishVerb,verbPerson,'Present Active') +"." )
    answer = latinNouns.getLatinNounForm(latinNoun,'nominative',subjectPlurality) + " " + latinVerbs.getLatinVerbForm(latinVerb,verbPerson,'Present Active')
    return (question,answer)
    
def twoWordAccusativeSentence(user_profile):
    #get a triplet - we'll ignore the nominative.
    #Use of gettriplet forces a transitive verb, which is good.
    words = quizUtility.getTriplet(user_profile)
    
    verbPerson = random.randrange(1,7)
    objectPlurality = random.choice( ('singular','plural') )

    question = (getEnglishPronoun(verbPerson).title() + " "
        + englishVerbs.getEnglishVerbForm(words[2],verbPerson,'Present Active') + " the "
        + englishNouns.getEnglishNounForm(words[1],objectPlurality))
    
    answer = ( latinNouns.getLatinNounForm(words[1].translation,'accusative',objectPlurality)
              + " " + latinVerbs.getLatinVerbForm(words[2].translation,verbPerson,'Present Active') )
    
    return (question,answer)


def getChapterThreeShortSentence(user_profile):
    subjectPlurality = random.choice( ('singular','plural') )
    objectPlurality = random.choice( ('singular','plural') )
    person = utility.getPerson(3,subjectPlurality)
    
    words = quizUtility.getTriplet(user_profile)
    
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