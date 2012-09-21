from django.db import models

class LatinConjugation(models.Model):
    #Currently, irregulars will be entirely separate conjugations.    
    name = models.CharField(max_length=100)
    def __unicode__(self):
        return self.name

class LatinVerb(models.Model):
    present = models.CharField(max_length=100)
    infinitive = models.CharField(max_length=100)
    perfect = models.CharField(max_length=100)
    pastparticiple = models.CharField(max_length=100)
    conjugation = models.ForeignKey(LatinConjugation)
    transitive = models.BooleanField(default=True)
    def __unicode__(self):
        return self.present
    
class LatinTense(models.Model):
    name = models.CharField(max_length=100)
    def __unicode__(self):
        return self.name
    
class LatinTable(models.Model):
    conjugation = models.ForeignKey(LatinConjugation)
    tense = models.ForeignKey(LatinTense)
    person1 = models.CharField(max_length=100)
    person2 = models.CharField(max_length=100)
    person3 = models.CharField(max_length=100)
    person4 = models.CharField(max_length=100)
    person5 = models.CharField(max_length=100)
    person6 = models.CharField(max_length=100)
    def __unicode__(self):
        return self.tense.name + ' of ' + self.conjugation.name