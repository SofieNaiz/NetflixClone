from django.db import models

  
class film(models.Model):
    movie_id = models.AutoField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=200, blank=False)
    yearRelease = models.DateField(blank=False)
    rating = models.IntegerField(blank=False)
    path = models.CharField(max_length=250, blank=False)
    filmType= models.CharField(max_length=250, blank=False)
    
class netflixUsers(models.Model):
    user_id = models.AutoField(primary_key=True, auto_created=True)
    fname = models.CharField(max_length=220, blank=False)
    lname = models.CharField(max_length=220, blank=False)
    email = models.CharField(max_length=220, blank=False)
    dob  = models.DateField(blank=False)
