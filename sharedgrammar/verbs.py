import utility

def makeVerbTableArray(theTable):
    #handles an english or latin table
    return (None,theTable.person1, theTable.person2, theTable.person3, theTable.person4, theTable.person5, theTable.person6)
    #None is because we don't want a zero-based array
    
def processVerb(verb,str):
    str = str.replace('[PP1]',verb.present)
    str = str.replace('[PP2]',verb.infinitive)
    str = str.replace('[PP3]',verb.perfect)
    str = str.replace('[PP4]',verb.pastparticiple)
    return utility.handleSyntax(str)
    