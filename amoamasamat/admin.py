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
admin.site.register(Level)

class LessonAdmin(admin.ModelAdmin):
    list_display = ('level','__unicode__')
    
admin.site.register(Lesson, LessonAdmin)

class EnglishNounAdmin(admin.ModelAdmin):
    filter_horizontal = ("properties",)
    


admin.site.register(EnglishNoun,EnglishNounAdmin)

from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from account.models import UserProfile

admin.site.unregister(User)

class UserProfileInline(admin.StackedInline):
    model = UserProfile

class UserProfileAdmin(UserAdmin):
    inlines = [ UserProfileInline, ]

admin.site.register(User, UserProfileAdmin)