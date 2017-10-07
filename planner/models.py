from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=255)

class Event(models.Model):
    title = models.CharField(max_length=255)
    day = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    location = models.ForeignKey(Location)
    note = models.TextField()
    author = models.ForeignKey(User)
    create_dt = models.DateTimeField(default=datetime.now())
