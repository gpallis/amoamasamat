from django.db import models
from englishgrammar.models import EnglishVerb,EnglishNoun

# Create your models here.
class Lesson(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    level = models.DecimalField(max_digits=5,decimal_places=2)
    def __unicode__(self):
        return self.title
    def get_absolute_url(self):
        return "/lessons/" + str(self.level) + "/"
    
class Level(models.Model):
    title = models.CharField(max_length=200)
    level_number = models.IntegerField()
    number_of_questions = models.IntegerField()
    question_generator = models.CharField(max_length=100,default="threeWordSentence")
    verb_unlocks = models.ManyToManyField(EnglishVerb,blank=True)
    noun_unlocks = models.ManyToManyField(EnglishNoun,blank=True)
    def __unicode__(self):
        return self.title