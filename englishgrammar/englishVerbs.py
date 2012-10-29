from englishgrammar.models import *
from sharedgrammar import verbs
import re

def getEnglishVerbForm(theVerb,thePerson,theTense):    
    verb = theVerb
    tenseObject = EnglishTense.objects.get(name=theTense)
    table = EnglishTable.objects.filter(conjugation=verb.conjugation).get(tense=tenseObject)
    tableWord = verbs.makeVerbTableArray(table)[thePerson]
    actualWord = verbs.processVerb(verb,tableWord)
    return actualWord