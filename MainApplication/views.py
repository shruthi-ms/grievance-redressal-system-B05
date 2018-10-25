from django.shortcuts import render
from . models import *
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random

def index(request):
	template = loader.get_template("MainApplication/try.html")
	x = Academics.objects.all()
	context = {
		'list' : x
	}
	return HttpResponse(template.render(context,request))

def Category(request):
	template = loader.get_template("MainApplication/category.html")
	m = LoggedInUser.objects.all()[0].userId
	u = User.objects.get(userRollNumber=m)
	X = u.academics_set.all()
	Y = Academics.objects.all()
	context = {
		"list" : X,
		"AllList" : Y
	}
	return HttpResponse(template.render(context,request))    

def Login(request):
	if request.method=='POST':
		try:
			x = login.objects.get(userName=request.POST['email'])
		except(KeyError, login.DoesNotExist):
			template = loader.get_template('MainApplication/try.html')
			context = {
					'IDinvalid':"Invalid Username !",
				}
			return HttpResponse(template.render(context,request))
		if request.POST['pass'] != x.paword:
			template = loader.get_template('MainApplication/try.html')
			context = {
					'Passwordinvalid':"Incorrect password!",
				}
			return HttpResponse(template.render(context,request))

		else:
			uid = x.userId.userRollNumber
			LoggedInUser.objects.all().delete()
			l = LoggedInUser()
			l.userId = uid
			l.save()
			template = loader.get_template('MainApplication/index.html')
			context = {
					'id' : x.userName,
					'pc' : x.paword
				}
			return HttpResponse(template.render(context,request))

def Profile(request):
	template = loader.get_template('MainApplication/profile.html')
	context = {

	}
	return HttpResponse(template.render(context,request))

def requestOtp(request):
	template = loader.get_template('MainApplication/profile.html')
	m = LoggedInUser.objects.all()[0].userId
	u = User.objects.get(userRollNumber=int(m))
	u.latestotp_set.all().delete()
	val = random.randint(1000,9999)
	u.latestotp_set.create(otp=val)	
	u = User.objects.get(userRollNumber=m)
	umi = u.UserMailId
	from_gmail_user = 'grs.sem5@gmail.com'
	from_gmail_password = 'grssem5@123'
	user = umi
	print(user)
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(from_gmail_user, from_gmail_password)
	print("logged in")
	msg = MIMEMultipart()
	msg['From'] = from_gmail_user
	msg['To'] = user
	msg['Subject'] = "GRS Notification - OTP"
	body = "One time otp for your settings is: " + str(val) 
	msg.attach(MIMEText(body, 'plain'))
	text = msg.as_string()
	server.sendmail(from_gmail_user, user, text)
	server.quit()
	context = {

	}
	return HttpResponse(template.render(context,request))

def validateOtp(request):
	template = loader.get_template('MainApplication/profile.html')
	m = LoggedInUser.objects.all()[0].userId
	u = User.objects.get(userRollNumber=int(m))
	l = u.latestotp_set.all()
	number = l[0].otp
	changedNumber = request.POST['mobile']
	x = request.POST['enterOtp']
	if(int(x)==number):
		msg = 'Validated'
		t = User.objects.get(userRollNumber=int(m))
		t.userMobileNumber = changedNumber
		t.save()
		from_gmail_user = 'grs.sem5@gmail.com'
		from_gmail_password = 'grssem5@123'
		m = LoggedInUser.objects.all()[0].userId
		u = User.objects.get(userRollNumber=m)
		user = u.UserMailId
		server = smtplib.SMTP('smtp.gmail.com', 587)
		server.starttls()
		server.login(from_gmail_user, from_gmail_password)
		print("logged in")
		msg = MIMEMultipart()
		msg['From'] = from_gmail_user
		msg['To'] = user
		msg['Subject'] = "GRS Notification - profile updation"
		body = "succesfully updated your profile" 
		msg.attach(MIMEText(body, 'plain'))
		text = msg.as_string()
		server.sendmail(from_gmail_user, user, text)
		server.quit()
		context = {
			'message': msg
		}
	else:
		msg = 'Not Validated'
		context = {
			'mess': msg
		}
	return HttpResponse(template.render(context,request))

def register(request):
	#get the current logged in user id
	m = LoggedInUser.objects.all()[0].userId
	u = User.objects.get(userRollNumber=m)
	x = request.POST['description']
	u.academics_set.create(description=x,acadId=300,userId=400,incharge=request.POST['incharge'],subcatId=request.POST['subcat']) 
	u.save()
	from_gmail_user = 'grs.sem5@gmail.com'
	from_gmail_password = 'grssem5@123'
	user = u.UserMailId
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(from_gmail_user, from_gmail_password)
	print("logged in")
	msg = MIMEMultipart()
	msg['From'] = from_gmail_user
	msg['To'] = user
	msg['Subject'] = "GRS Notification"
	body = "Complaint filed by: " + user + ", description: " + x
	msg.attach(MIMEText(body, 'plain'))
	text = msg.as_string()
	server.sendmail(from_gmail_user, user, text)
	server.quit()
	template = loader.get_template('MainApplication/category.html')
	m = LoggedInUser.objects.all()[0].userId
	u = User.objects.get(userRollNumber=m)
	X = u.academics_set.all()
	Y = Academics.objects.all()
	context = {
		"list" : X,
		"AllList" : Y
	}
	return HttpResponse(template.render(context,request))