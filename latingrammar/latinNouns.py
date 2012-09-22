from latingrammar.models import *
from sharedgrammar import utility

def processLatinNoun(noun,str):
    str = str.replace('[PP1]',noun.nominativeSingular)
    str = str.replace('[PP2]',noun.genitiveSingular)
    return utility.handleSyntax(str)

def getNounEnding(nounTable,fieldName):
    endings = {
        'nominativesingular':nounTable.nominativeSingular,
        'vocativesingular':nounTable.vocativeSingular,
        'accusativesingular':nounTable.accusativeSingular,
        'genitivesingular':nounTable.genitiveSingular,
        'dativesingular':nounTable.dativeSingular,
        'ablativesingular':nounTable.ablativeSingular,
        'nominativeplural':nounTable.nominativePlural,
        'vocativeplural':nounTable.vocativePlural,
        'accusativeplural':nounTable.accusativePlural,
        'genitiveplural':nounTable.genitivePlural,
        'dativeplural':nounTable.dativePlural,
        'ablativeplural':nounTable.ablativePlural,
    }
    return endings[fieldName.lower()]

def getLatinNounForm(theNoun,theCase,theNumber):
    #thenoun is the actual NOUN object, the other two are strings
    theCase = theCase.lower()
    theNumber = theNumber.lower()
    #Just in case of error.
    nounTable = LatinNounTable.objects.get(declension=theNoun.declension)
    ending = getNounEnding(nounTable,(theCase+theNumber))
    
    return processLatinNoun(theNoun,ending)