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

class Subcategory(models.Model):
	sc = models.CharField(max_length = 45)

class Academics(models.Model):
	acadId = models.IntegerField()
	userId = models.ForeignKey(User, on_delete = models.CASCADE)
	subcatId = models.CharField(max_length=45)
	incharge = models.CharField(max_length=45)
	description = models.CharField(max_length = 350)
	def __str__(self):
		return 'Complaint: ' + str(self.description) + ', Incharge: ' + str(self.incharge)

class latestOtp(models.Model):
	userId = models.ForeignKey(User, on_delete = models.CASCADE)
	otp = models.IntegerField()