import re

def handleSyntax(str):
    #this needs to move to a sharedgrammar app.
    
    hyphens = len(re.findall('-',str))
    #this stores the NUMBER of hyphens
    
    if (hyphens > 0):
        root = str.split('-')[0]
        ending = str.split('-')[-1]
        root = root[:-hyphens] #chop off letters equal to number of hyphens
        return root+ending
    else:
        #that was easy - we just got told what to return (i.e. an irregular)
        return str
