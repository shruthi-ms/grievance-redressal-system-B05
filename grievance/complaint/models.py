# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Academics(models.Model):
	acadId = models.AutoField(primary_key=True)
	userId = models.IntegerField()
	subcatId = models.IntegerField()
	incharge = models.CharField(max_length=45)
	description = models.CharField(max_length = 400)

	def __str__(self):
		return 'ComplaintId:A' + str(self.subcatId) + str(self.pk) + ' Incharge: ' + str(self.incharge)

class Sports(models.Model):
	sportsId = models.AutoField(primary_key=True)
	userId = models.IntegerField()
	subcatId = models.IntegerField()
	sportname = models.CharField(max_length=45)
	nature = models.CharField(max_length=45)
	description = models.CharField(max_length = 400)

	def __str__(self):
		return 'ComplaintId:S' + str(self.subcatId) + str(self.pk) + ' Sportname: ' + str(self.sportname)