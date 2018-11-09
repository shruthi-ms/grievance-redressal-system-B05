# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
	userRollNumber = models.IntegerField()
	userFName = models.CharField(max_length = 45)
	userLName = models.CharField(max_length = 45)
	userMobileNumber = models.CharField(max_length = 10)
	UserUg = models.CharField(max_length = 10)
	UserMailId = models.CharField(max_length = 45)
	
	def __str__(self):
		return 'Id : ' + str(self.userRollNumber) + ' ; Name : ' + self.userFName + ' ' + self.userLName
class login(models.Model):
	userId = models.ForeignKey(User, on_delete = models.CASCADE)
	userName = models.CharField(max_length = 45)
	paword = models.CharField(max_length = 45)
	status = models.IntegerField(default = 0)

class LoggedInUser(models.Model):
	userId = models.IntegerField()

	def __str__(self):
		return str(self.userId)

class Academics(models.Model):
	acadId = models.AutoField(primary_key=True)
	userId = models.ForeignKey(User, on_delete = models.CASCADE)
	subcatId = models.IntegerField(default=0)
	incharge = models.CharField(max_length=45)
	description = models.CharField(max_length = 400)

	def __str__(self):
		return 'ComplaintId:A' + str(self.subcatId) + str(self.pk) + ' Incharge: ' + str(self.incharge)

class latestOtp(models.Model):
	userId = models.ForeignKey(User, on_delete = models.CASCADE)
	otp = models.IntegerField()

class Sports(models.Model):
	sportsId = models.AutoField(primary_key=True)
	userId = models.ForeignKey(User, on_delete = models.CASCADE)
	subcatId = models.IntegerField(default=0)
	sportname = models.CharField(max_length=45)
	nature = models.CharField(max_length=45)
	description = models.CharField(max_length = 400)

	def __str__(self):
		return 'ComplaintId:S' + str(self.subcatId) + str(self.pk) + ' Sportname: ' + str(self.sportname)

class Events(models.Model):
	eventId = models.AutoField(primary_key=True)
	userId = models.ForeignKey(User, on_delete = models.CASCADE)
	subcatId = models.IntegerField(default=0)
	eventname = models.CharField(max_length=45)
	#fromdate = models.DateTimeField()
	#todate = models.DateTimeField()
	nature = models.CharField(max_length=45)
	description = models.CharField(max_length = 400)

	def __str__(self):
		return 'ComplaintId:E' + str(self.subcatId) + str(self.pk) + ' Eventname: ' + str(self.eventname)

class Hostel(models.Model):
	hostelId = models.AutoField(primary_key=True)
	userId = models.ForeignKey(User, on_delete = models.CASCADE)
	subcatId = models.IntegerField(default=0)
	incharge = models.CharField(max_length=45)
	hostelRoomNo = models.CharField(max_length=6)
	description = models.CharField(max_length = 400)

	def __str__(self):
		return 'ComplaintId:H' + str(self.subcatId) + str(self.pk) + ' description: ' + str(self.description)

class Others(models.Model):
	othersId = models.AutoField(primary_key=True)
	userId = models.ForeignKey(User, on_delete = models.CASCADE)
	description = models.CharField(max_length = 400)

	def __str__(self):
		return 'ComplaintId:O' + str(self.pk) + ' description: ' + str(self.description)

class Questions(models.Model):
	questionId = models.AutoField(primary_key=True)
	ComplaintId = models.CharField(max_length=45)
	question = models.CharField(max_length = 400)
	pub_date = models.DateTimeField()
	active_till = models.DateTimeField()
	
	def __str__(self):
		return self.question


class Choice(models.Model):
	qid = models.ForeignKey(Questions, on_delete=models.CASCADE)
	ChoiceOption = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)
	def __str__(self):
		return self.ChoiceOption

class table_complaint(models.Model):
	gid = models.AutoField(primary_key=True)
	qaId = models.IntegerField(default=0)
	userId = models.IntegerField(default=0)
	Compid = models.CharField(max_length=45)
	description = models.CharField(max_length=400)
	status = models.CharField(max_length=45)
	poll = models.CharField(max_length=30)