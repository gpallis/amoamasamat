from django.db import models
from django.contrib.auth.models import User
from englishgrammar.models import EnglishVerb

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    level = models.IntegerField(default=1)
    xp = models.IntegerField(default=0)
    knownVerbs = models.ManyToManyField(EnglishVerb)
    
User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
