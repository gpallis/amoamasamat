from django.db import models
from latingrammar.models import LatinVerb

class EnglishConjugation(models.Model):
    #Currently, irregulars will be entirely separate conjugations.    
    name = models.CharField(max_length=100)
    def __unicode__(self):
        return self.name

class EnglishVerb(models.Model):
    translation = models.OneToOneField(LatinVerb)
    present = models.CharField(max_length=100)
    infinitive = models.CharField(max_length=100)
    perfect = models.CharField(max_length=100)
    pastparticiple = models.CharField(max_length=100)
    conjugation = models.ForeignKey(EnglishConjugation)
    def __unicode__(self):
        return self.present
    
class EnglishTense(models.Model):
    name = models.CharField(max_length=100)
    def __unicode__(self):
        return self.name
    
class EnglishTable(models.Model):
    conjugation = models.ForeignKey(EnglishConjugation)
    tense = models.ForeignKey(EnglishTense)
    person1 = models.CharField(max_length=100)
    person2 = models.CharField(max_length=100)
    person3 = models.CharField(max_length=100)
    person4 = models.CharField(max_length=100)
    person5 = models.CharField(max_length=100)
    person6 = models.CharField(max_length=100)
    def __unicode__(self):
        return self.tense.name + ' of ' + self.conjugation.name
