from django.db import models
from datetime import datetime

# Create your models here.


class Events(models.Model):
    event_name = models.CharField(max_length=20)
    event_date = models.DateTimeField()
    event_location = models.CharField(max_length=20)
    event_description = models.TextField(max_length=400)
    event_image = models.ImageField(upload_to="events/images/")
    # event_link = models.CharField(max_length=200)
    # event_host = models.ForeignKey(User, related_name="event_host")
    def __str__(self):
        return self.event_name


class Register(models.Model):
    userid = models.CharField(max_length=15)
    # lname=models.CharField(max_length=15)
    email = models.CharField(max_length=40)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.userid


class eve_register(models.Model):
    userid = models.CharField(max_length=15)
    event = models.CharField(max_length=20)

    def __str__(self):
        return self.userid


class feedback(models.Model):
    message = models.CharField(max_length=80)
    fname = models.CharField(max_length=15)
    lname = models.CharField(max_length=15)
    email = models.CharField(max_length=40)

    def __str__(self):
        return self.lname


class RegisterOrganizer(models.Model):
    userid = models.CharField(max_length=15)
    email = models.CharField(max_length=40)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.userid
