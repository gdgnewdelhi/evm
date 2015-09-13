from django.db import models
from django.contrib.auth.user.models import User
from events.models import Event
# Create your models here.

class Attendee(models.Model):
	attendee = models.ForeignKeyField(User)
	address = models.CharField(max_length = 1000, default = None)
	profession = models.CharField()
	phone_number = models.PositiveIntegerfield(default = None)

class EventAttendee(models.Model):
	"""
	Model class for relationship between the events and attendees
	"""
	attendee = models.ForeignKeyField(Attendee)
	event = models.ForeignKeyField(Event)

