from django.db import models

# Create your models here.
class Lesson(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    level = models.DecimalField(max_digits=5,decimal_places=2)
    def __unicode__(self):
        return self.title
    
class Level(models.Model):
    title = models.CharField(max_length=200)
    level_number = models.IntegerField()
    number_of_questions = models.IntegerField()
    def __unicode__(self):
        return self.title