from latingrammar.models import *
from sharedgrammar import utility

def processLatinNoun(noun,str):
    str = str.replace('[PP1]',noun.nominativeSingular)
    str = str.replace('[PP2]',noun.genitiveSingular)
    return utility.handleSyntax(str)

def getNounEnding(nounTable,case,person):
    fieldName = case.lower() + person.title()
    return getattr(nounTable,fieldName)

def getLatinNounForm(theNoun,theCase,theNumber):
    #thenoun is the actual NOUN object, the other two are strings

    nounTable = LatinNounTable.objects.get(declension=theNoun.declension)
    ending = getNounEnding(nounTable,theCase,theNumber)
    
    return processLatinNoun(theNoun,ending)