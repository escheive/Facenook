from django.db import models
from datetime import date
from django.contrib.auth.models import User

# Create post model

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    content = models.CharField(max_length=250)
    comments = models.CharField(max_length=250)
    likes = models.CharField(max_length=250)

    def __str__(self):
        return self.user + self.content.truncatechars(5)

# Create a profile model and link it to built-in django user model so that more info can be stored about the existing User model thats not related to authentication
# Cited source at bottom
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)


# Profile model was created based on tutorial from this site:
# https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#onetoone