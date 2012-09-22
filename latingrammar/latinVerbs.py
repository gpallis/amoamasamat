from latingrammar.models import *
from sharedgrammar import verbs
    
def getLatinVerbForm(theVerb,thePerson,theTense):
    #thenoun is the actual VERB object
    verb = theVerb
    tenseObject = LatinTense.objects.get(name=theTense)
    table = LatinTable.objects.filter(conjugation=verb.conjugation).get(tense=tenseObject)
    tableWord = verbs.makeVerbTableArray(table)[thePerson]
    actualWord = verbs.processVerb(verb,tableWord)
    return actualWord