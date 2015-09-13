from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Event(models.Model):
	"""
	Model class for Events that are being organized
	"""
	name = models.CharField(max_length = 200, default = None)
	title = models.CharField(max_length = 200, default = None)
	description = models.CharField(max_length = 5000, default = None)
	start_date_time = models.DateTimeField(default = None)
	end_date_time = models.DateTimeField(max_length = 200, default = None)
	no_of_attendee = models.PositiveIntegerField(max_length = 200, default = None)

class Speaker(models.Model):
	"""
	Model class for Speakers who speak at any of the conducted events 
	"""
	STUDENT = 'ST'
	SOFTWARE_ENGINEER = 'SDE'
	TEACHER = 'TE'
	FREELANCER = 'FR'
	DESIGNER = 'DE'
	OTHERS = 'OT'
	PROFESSION_CHOICES = (
		(STUDENT, 'Student'),
		(SOFTWARE_ENGINEER, 'Software Engineer'),
		(TEACHER, 'Teacher'),
		(FREELANCER, 'Freelancer'),
		(DESIGNER, 'Designer'),
		(OTHERS, 'Others'),
	)
	user = models.ForeignKeyField(User)
	profession = models.CharField(max_length=3, choices=PROFESSION_CHOICES, default=OTHERS)
	address = models.CharField()
	phone_number = models.PositiveIntegerField()
	website = models.UrlField()
	blog = models.UrlField()
	github = models.UrlField()
	linkedin = models.UrlField()

class EventSpeaker(models.Model):
	"""
	Model class for relationship between the events and speakers
	"""
	speaker = models.ForeignKeyField(Speaker)
	event = models.ForeignKeyField(Event)
