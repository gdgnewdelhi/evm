from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Event(models.Model):
	name = models.CharField(max_length = 200, default = None)
	title = models.CharField(max_length = 200, default = None)
	description = models.CharField(max_length = 5000, default = None)
	start_date_time = models.DateTimeField(default = None)
	end_date_time = models.DateTimeField(max_length = 200, default = None)
	no_of_attendee = models.PositiveIntegerField(max_length = 200, default = None)
	speaker = models.ForeignKeyField(User)

