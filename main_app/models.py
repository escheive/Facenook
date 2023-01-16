from django.db import models
from datetime import date
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create post model

class Post(models.Model):
    user = models.ForeignKey(User, related_name="posts", on_delete=models.DO_NOTHING)
    content = models.CharField(max_length=140)
    comments = models.CharField(max_length=250, null=True)
    likes = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (
            f"{self.user} "
            f"({self.created_at:%Y-%m-%d %H:%M}): "
            f"{self.content[:30]}..."
        )


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follows = models.ManyToManyField(
        "self", related_name="followed_by", symmetrical=False, blank=True
    )

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()
        user_profile.follows.add(instance.profile)
        user_profile.save()

# Create a profile model and link it to built-in django user model so that more info can be stored about the existing User model thats not related to authentication
# Cited source at bottom
# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     bio = models.TextField(max_length=500, blank=True)
#     location = models.CharField(max_length=30, blank=True)
#     birth_date = models.DateField(null=True, blank=True)

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()

# Profile model was created based on tutorial from this site:
# https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#onetoone