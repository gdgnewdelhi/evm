from django.db import models
from django.contrib.auth.user.models import User

# Create your models here.

class Attendee(models.Model):
	attendee = models.ForeignKeyField(User)
	address = models.CharField(max_length = 1000, default = None)
	profession = models.CharField()
	phone_number = models.PositiveIntegerfield(default = None)
