from django.http import HttpResponse
from django.shortcuts import render
#from latingrammar import actions
#
#def home(request):
#    verbForm = actions.getLatinVerbForm('amo',2,'Present Active')
#    return render(request,'showVerb.html',{'theVerb':verbForm})

def home(request):
    return HttpResponse('ugh')