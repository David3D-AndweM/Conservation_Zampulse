import uuid
from datetime import datetime

from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField(primary_key=True, default=0)
    bio = models.TextField(blank=True, default='')
    profileing = models.ImageField(upload_to='profile_images', default='profile-picturePlaceholder.jpg')
    location = models.CharField(max_length=100, blank=True, default='')

    def __str__(self):
        return self.user.username


class Story(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4())
    user = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post-')
    caption = models.TextField()
    challenge = models.TextField()
    short_description = models.TextField()
    full_description = models.TextField()
    location = models.CharField(max_length=100, default='')
    google_map_link = models.URLField(max_length=200, default='https://maps.google.com')
    created_at = models.DateTimeField(default=datetime.now)
    no_of_likes = models.IntegerField(default=0)
    category = models.CharField(max_length=100, choices=[
        ('Wildlife Conservation', 'Wildlife Conservation'),
        ('Environmental Conservation', 'Environmental Conservation'),
        ('Sustainable Development', 'Sustainable Development'),
        ('Community Engagement', 'Community Engagement'),
        ('Other', 'Other')])


    def __str__(self):
        return self.user
