from django.db import models

class Result(models.Model):
    year = models.IntegerField()
    from_year = models.IntegerField()
    to_year = models.IntegerField()
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)

class Event(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField()

class EventCategory(models.Model):
    name = models.CharField(max_length=255)
