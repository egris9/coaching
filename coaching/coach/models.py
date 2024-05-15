from django.db import models
from django.contrib.auth.models import User



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')

    class Type(models.TextChoices):
        Client = 'client'
        Coache = 'coach'

    def __str__(self):
        return self.type

    type = models.CharField(max_length=7, choices=Type.choices, default=Type.Client)

class Training_plan(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    Profile = models.OneToOneField(User, on_delete=models.CASCADE)
    categorie = models.CharField(max_length=100)

class Training_session(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()   
    training_plan = models.ForeignKey(Training_plan, on_delete=models.CASCADE) 
    location = models.CharField(max_length=100)
    participant_limit = models.IntegerField()
    

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    session = models.ForeignKey(Training_session, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    
