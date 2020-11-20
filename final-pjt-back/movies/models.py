from django.db import models

class Genre(models.Model):
  name = models.CharField(max_length=50)

class Movie(models.Model):
  movie_no = models.IntegerField()
  title = models.CharField(max_length=100)
  release_date = models.DateField()
  poster_path = models.CharField(max_length=200)
  adult = models.BooleanField(default=False)
  overview = models.TextField()
  vote_count = models.IntegerField(default=0)
  rate = models.FloatField(default=0.0)
  genres = models.ManyToManyField(Genre, related_name='movie_genres')
  status = models.BooleanField(default=False)
  admin_reg = models.BooleanField(default=False)