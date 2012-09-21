from englishgrammar.models import *
import re

def makeTableArray(theTable):
        return (None,theTable.person1, theTable.person2, theTable.person3, theTable.person4, theTable.person5, theTable.person6)
        #None is because we don't want a zero-based array
        
def processString(verb,str):
    str = str.replace('[PP1]',verb.present)
    hyphens = len(re.findall('-',str))
    #specifically, the NUMBER of hyphens
    
    if (hyphens > 0):
        root = str.split('-')[0]
        ending = str.split('-')[-1]
        root = root[:-hyphens] #chop off letters equal to number of hyphens
        return root+ending
    else:
        #that was easy - we just got told what to return (i.e. an irregular)
        return str

def getEnglishVerbForm(theVerb,thePerson,theTense):
    
    verb = theVerb
    tenseObject = EnglishTense.objects.get(name=theTense)
    table = EnglishTable.objects.filter(conjugation=verb.conjugation).get(tense=tenseObject)
    tableWord = makeTableArray(table)[thePerson]
    actualWord = processString(verb,tableWord)
    return actualWord