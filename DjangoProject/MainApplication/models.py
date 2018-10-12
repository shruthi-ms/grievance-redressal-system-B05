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
		return 'Id : ' + str(self.userId) + ' ; Name : ' + self.userFName + ' ' + self.userLName

class login(models.Model):
	#userId = models.ForeignKey(User, on_delete = models.CASCADE)
	userName = models.CharField(max_length = 45)
	paword = models.CharField(max_length = 45)

class Academics(models.Model):
	acadId = models.IntegerField()
	userId = models.IntegerField()
	subcatId = models.IntegerField()
	incharge = models.CharField(max_length=45)
	description = models.CharField(max_length = 350)

	def __str__(self):
		return 'Complaint: ' + str(self.description) + ', Incharge: ' + str(self.incharge)