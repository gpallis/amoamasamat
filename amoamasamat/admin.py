from django.contrib import admin
from latingrammar.models import LatinVerb,LatinTense,LatinConjugation,LatinTable
from englishgrammar.models import EnglishVerb,EnglishTense,EnglishConjugation,EnglishTable

admin.site.register(LatinVerb)
admin.site.register(LatinTense)
admin.site.register(LatinConjugation)
admin.site.register(LatinTable)
admin.site.register(EnglishVerb)
admin.site.register(EnglishTense)
admin.site.register(EnglishConjugation)
admin.site.register(EnglishTable)
