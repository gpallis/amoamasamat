from django.contrib import admin
from latingrammar.models import LatinVerb,LatinTense,LatinConjugation,LatinTable,LatinDeclension,LatinNoun,LatinNounTable
from englishgrammar.models import EnglishVerb,EnglishTense,EnglishConjugation,EnglishTable,EnglishNoun

admin.site.register(LatinVerb)
admin.site.register(LatinTense)
admin.site.register(LatinConjugation)
admin.site.register(LatinTable)
admin.site.register(LatinNoun)
admin.site.register(LatinDeclension)
admin.site.register(LatinNounTable)
admin.site.register(EnglishVerb)
admin.site.register(EnglishTense)
admin.site.register(EnglishConjugation)
admin.site.register(EnglishTable)
admin.site.register(EnglishNoun)