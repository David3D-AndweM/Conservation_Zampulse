# events/models.py
from django.db import models
from django.conf import settings

class Event(models.Model):
    EVENT_TYPE_CHOICES = [
        ('online', 'Online Meeting'),
        ('gather', 'Gather'),
        ('field', 'Field Event'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=200)
    event_type = models.CharField(max_length=50, choices=EVENT_TYPE_CHOICES)
    organizer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='events_organized')
    attendees = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='events_attending')

    def __str__(self):
        return self.name
