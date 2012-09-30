from django.contrib import admin
from latingrammar.models import *
from englishgrammar.models import *
from sharedgrammar.models import *
from lessons.models import *

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
admin.site.register(NounProperty)
admin.site.register(Lesson)

class EnglishNounAdmin(admin.ModelAdmin):
    filter_horizontal = ("properties",)

admin.site.register(EnglishNoun,EnglishNounAdmin)
