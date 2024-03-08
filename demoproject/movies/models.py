from django.db import models

# Create your models here.
class Movie(models.Model):
 # each class variable represents a database i.e. table field in the model
  title = models.CharField(max_length=200)
  director = models.CharField(max_length=30)
  release_date = models.DateTimeField('release date')
  genre = models.CharField(max_length=200)
  duration = models.FloatField()
  
  def __str__(self):
        return self.title + " - " + self.director
        
  @property
  def is_post_production_completed(self):
   return self.duration > 0