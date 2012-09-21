from latingrammar.models import *
import re

def getLatinVerbForm(theVerb,thePerson,theTense):
    
    verb = Verb.objects.get(present=theVerb)
    tenseObject = Tense.objects.get(name=theTense)
    table = Table.objects.filter(conjugation=verb.conjugation).get(tense=tenseObject)
    tableWord = makeTableArray(table)[thePerson]
    actualWord = processString(verb,tableWord)
    return actualWord
    
    def makeTableArray(theTable):
        return (None,theTable.person_1, theTable.person_2, theTable.person_3, theTable.person_4, theTable.person_5, theTable.person_6)
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