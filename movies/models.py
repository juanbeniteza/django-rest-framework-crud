from django.db import models

 # Create Movie Model
class Movie(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    year = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True) # When it was create
    updated_at = models.DateTimeField(auto_now=True) # When i was update
    creator = models.ForeignKey('auth.User', related_name='movies', on_delete=models.CASCADE)





