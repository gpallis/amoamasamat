from django.db import models
from django.contrib.auth.models import User
from englishgrammar.models import EnglishVerb,EnglishNoun

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    level = models.IntegerField(default=1)
    xp = models.IntegerField(default=0)
    known_verbs = models.ManyToManyField(EnglishVerb)
    known_nouns = models.ManyToManyField(EnglishNoun)
    
    
User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
