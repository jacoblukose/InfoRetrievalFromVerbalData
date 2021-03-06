from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
   firstname = models.CharField(max_length=50)
   lastname = models.CharField(max_length=50)
   email = models.CharField(max_length=50,primary_key=True)
   password = models.CharField(max_length=100)

   def __unicode__(self):
    	return self.email

class Audio(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.FileField(upload_to="audio")
	email = models.ForeignKey(User)
	numOfSpeakers = models.IntegerField(default=1)

	def __unicode__(self):
		return self.name.name

class Diarization(models.Model):
	Diarization_id = models.ForeignKey(Audio)
	Speaker_id = models.IntegerField()

	def __unicode__(self):
	   	return self.Diarization_id
