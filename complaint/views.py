# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your views here.
from django.shortcuts import render
from . models import *
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def index(request):
	template = loader.get_template("complaint/login.html")
	#x = academics.objects.all()
	context = {
	#	'list' : x
	}
	return HttpResponse(template.render(context,request))

def Login(request):
	if request.method=='POST':
		#Check if the username and password are valid
		try:
			x = login.objects.get(userName=request.POST['email'])
		except(KeyError, login.DoesNotExist):
			template = loader.get_template('complaint/login.html')
			context = {
					'IDinvalid':"Invalid Username !",
				}
			return HttpResponse(template.render(context,request))
		if request.POST['pass'] != x.paword:
			template = loader.get_template('complaint/login.html')
			context = {
					'Passwordinvalid':"Incorrect password!",
				}
			return HttpResponse(template.render(context,request))
		#if credentials are valid, login
		else:
			uid = x.userId.userRollNumber
			LoggedInUser.objects.all().delete()
			l = LoggedInUser()
			l.userId = uid
			l.save()
			template = loader.get_template('complaint/home.html')
			context = {
					'id' : x.userName,
					'pc' : x.paword
				}
			return HttpResponse(template.render(context,request))

#Academics
def Category(request):
	template = loader.get_template("complaint/academics.html")
	#get the id of current logged in user
	m = LoggedInUser.objects.all()[0].userId
	u = User.objects.get(userRollNumber=m)
	X = u.academics_set.all()
	Y = Academics.objects.all()
	#get the username
	uname = u.login_set.all()[0].userName
	context = {
		"uname" : uname,
		"list" : X,
		"AllList" : Y
	}
	return HttpResponse(template.render(context,request))

#Sports
def Category2(request):
	template = loader.get_template("complaint/sports.html")
	m = LoggedInUser.objects.all()[0].userId
	u = User.objects.get(userRollNumber=m)
	X = u.sports_set.all()
	Y = Sports.objects.all()
	uname = u.login_set.all()[0].userName
	context = {
		"uname" : uname,
		"list" : X,
		"AllList" : Y
	}
	return HttpResponse(template.render(context,request))    

#Events
def Category3(request):
	template = loader.get_template("complaint/events.html")
	m = LoggedInUser.objects.all()[0].userId
	u = User.objects.get(userRollNumber=m)
	X = u.events_set.all()
	Y = Events.objects.all()
	uname = u.login_set.all()[0].userName
	context = {
		"uname" : uname,
		"list" : X,
		"AllList" : Y
	}
	return HttpResponse(template.render(context,request))

#Hostel
def Category4(request):
	template = loader.get_template("complaint/hostel.html")
	m = LoggedInUser.objects.all()[0].userId
	u = User.objects.get(userRollNumber=m)
	X = u.hostel_set.all()
	Y = Hostel.objects.all()
	uname = u.login_set.all()[0].userName
	context = {
		"uname" : uname,
		"list" : X,
		"AllList" : Y
	}
	return HttpResponse(template.render(context,request))    

#Others
def Category5(request):
	template = loader.get_template("complaint/others.html")
	m = LoggedInUser.objects.all()[0].userId
	u = User.objects.get(userRollNumber=m)
	X = u.others_set.all()
	Y = Others.objects.all()
	uname = u.login_set.all()[0].userName
	context = {
		"uname" : uname,
		"list" : X,
		"AllList" : Y
	}
	return HttpResponse(template.render(context,request))    

#Academics Register form
def aform(request):
	template = loader.get_template("complaint/acad_register.html")
	m = LoggedInUser.objects.all()[0].userId
	u = User.objects.get(userRollNumber=m)
	uname = u.login_set.all()[0].userName
	context = {
		"uname" : uname
	}
	return HttpResponse(template.render(context,request))

#Sports Register form
def sform(request):
	template = loader.get_template("complaint/sport_register.html")
	m = LoggedInUser.objects.all()[0].userId
	u = User.objects.get(userRollNumber=m)
	uname = u.login_set.all()[0].userName
	context = {
		"uname" : uname
	}
	return HttpResponse(template.render(context,request))

#Events Register form
def eform(request):
	template = loader.get_template("complaint/event_register.html")
	m = LoggedInUser.objects.all()[0].userId
	u = User.objects.get(userRollNumber=m)
	uname = u.login_set.all()[0].userName
	context = {
		"uname" : uname
	}
	return HttpResponse(template.render(context,request))

#Hostel Register form
def hform(request):
	template = loader.get_template("complaint/hostel_register.html")
	m = LoggedInUser.objects.all()[0].userId
	u = User.objects.get(userRollNumber=m)
	uname = u.login_set.all()[0].userName
	context = {
		"uname" : uname
	}
	return HttpResponse(template.render(context,request))

#Others Register form
def oform(request):
	template = loader.get_template("complaint/others_register.html")
	m = LoggedInUser.objects.all()[0].userId
	u = User.objects.get(userRollNumber=m)
	uname = u.login_set.all()[0].userName
	context = {
		"uname" : uname
	}
	return HttpResponse(template.render(context,request))

#Academics reg'n confirmation
def acad_confirm(request):
	#get the current logged in user id
	m = LoggedInUser.objects.all()[0].userId
	u = User.objects.get(userRollNumber=m)
	x = request.POST['description']
	if request.POST['subcat'] == 'Library':
		v = 1
	if request.POST['subcat'] == 'Scholarship/Placement':
		v = 2
	if request.POST['subcat'] == 'Course':
		v = 3
	else:
		v = 4
	u.academics_set.create(description=x,userId=400,incharge=request.POST['incharge'],subcatId=v) 
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
	template = loader.get_template('complaint/acad_register.html')
	m = LoggedInUser.objects.all()[0].userId
	u = User.objects.get(userRollNumber=m)
	X = u.academics_set.all()
	Y = Academics.objects.all()
	V = Academics.objects.get(description=x)
	context = {
		"success" : 'Thanks for submission',
		"confirm" : V,
		"list" : X,
		"AllList" : Y
	}
	return HttpResponse(template.render(context,request))

#Profile settings page
def Profile(request):
	template = loader.get_template('complaint/profile.html')
	m = LoggedInUser.objects.all()[0].userId
	u = User.objects.get(userRollNumber=m)
	uname = u.login_set.all()[0].userName
	context = {
		"uname" : uname
	}
	return HttpResponse(template.render(context,request))

#Otp generating
def requestOtp(request):
	template = loader.get_template('complaint/profile.html')
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
	m = LoggedInUser.objects.all()[0].userId
	u = User.objects.get(userRollNumber=m)
	uname = u.login_set.all()[0].userName
	context = {
		"uname" : uname
	}
	return HttpResponse(template.render(context,request))

#Validating the otp
def validateOtp(request):
	template = loader.get_template('complaint/profile.html')
	m = LoggedInUser.objects.all()[0].userId
	u = User.objects.get(userRollNumber=int(m))
	l = u.latestotp_set.all()
	number = l[0].otp
	changedNumber = request.POST['mobile']
	changedUName = request.POST['username']
	x = request.POST['enterOtp']
	if(int(x)==number):
		msg = 'Validated'
		#t = User.objects.get(userRollNumber=int(m))
		if(changedNumber != ''):
			t = User.objects.get(userRollNumber=int(m))
			t.userMobileNumber = changedNumber
			t.save()
		if(changedUName != ''):
			print('changing userName')
			t = User.objects.get(userRollNumber=int(m))
			#t.userName = changedUName
			l = t.login_set.all()[0]
			l1 = l.paword
			l2 = l.status
			t.login_set.all().delete()
			t.login_set.create(userName=changedUName,paword=l1,status=l2)
			print(t.login_set.all()[0].userName)
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

#Sports reg'n confirmation
def sport_confirm(request):
	m = LoggedInUser.objects.all()[0].userId
	u = User.objects.get(userRollNumber=m)
	xs = request.POST['description']
	ys = u.UserMailId
	if request.POST['subcat'] == 'Indoor':
		v = 5
	if request.POST['subcat'] == 'Outdoor':
		v = 6

	u.sports_set.create(description=xs,userId=400,sportname=request.POST['spname'],subcatId=v) 
	u.save()

	from_gmail_user = 'grs.sem5@gmail.com'
	from_gmail_password = 'grssem5@123'
	user = ys
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(from_gmail_user, from_gmail_password)
	print("logged in")
	msg = MIMEMultipart()
	msg['From'] = from_gmail_user
	msg['To'] = user
	msg['Subject'] = "GRS Notification"
	body = "Complaint filed by: " + user + ", description: " + xs
	msg.attach(MIMEText(body, 'plain'))
	text = msg.as_string()
	server.sendmail(from_gmail_user, user, text)
	server.quit()

	template = loader.get_template('complaint/sport_register.html')
	
	Xs= Sports.objects.get(description=xs)
	m = LoggedInUser.objects.all()[0].userId
	u = User.objects.get(userRollNumber=m)
	uname = u.login_set.all()[0].userName
	context = {
		"success":'Thanks for Submission.',
		'list': Xs,
		"uname" : uname
	}
	return HttpResponse(template.render(context,request))

#Events reg'n confirmation
def event_confirm(request):
	m = LoggedInUser.objects.all()[0].userId
	u = User.objects.get(userRollNumber=m)
	xs = request.POST['description']
	nature = request.POST['nat']
	ys = u.UserMailId
	v=0
	if request.POST['subcat'] == 'Academic':
		v = 5
	if request.POST['subcat'] == 'Non-academic':
		v = 6

	u.events_set.create(description=xs,userId=400,eventname=request.POST['ename'],subcatId=v,nature=nature) 
	u.save()

	from_gmail_user = 'grs.sem5@gmail.com'
	from_gmail_password = 'grssem5@123'
	user = ys
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(from_gmail_user, from_gmail_password)
	print("logged in")
	msg = MIMEMultipart()
	msg['From'] = from_gmail_user
	msg['To'] = user
	msg['Subject'] = "GRS Notification"
	body = "Complaint filed by: " + user + ", description: " + xs
	msg.attach(MIMEText(body, 'plain'))
	text = msg.as_string()
	server.sendmail(from_gmail_user, user, text)
	server.quit()

	template = loader.get_template('complaint/event_register.html')
	
	Xs= Events.objects.get(description=xs)
	m = LoggedInUser.objects.all()[0].userId
	u = User.objects.get(userRollNumber=m)
	uname = u.login_set.all()[0].userName
	context = {
		"success":'Thanks for Submission.',
		'list': Xs,
		"uname" : uname
	}
	return HttpResponse(template.render(context,request))

#Hostel reg'n confirmation
def hostel_confirm(request):
	m = LoggedInUser.objects.all()[0].userId
	u = User.objects.get(userRollNumber=m)
	xs = request.POST['description']
	incharge = request.POST['hname']
	roomno = request.POST['roomno']
	ys = u.UserMailId
	v=0
	if request.POST['subcat'] == 'Accomodatiom':
		v = 7
	if request.POST['subcat'] == 'Mess':
		v = 8
	if request.POST['subcat'] == 'Transport':
		v = 9
	if request.POST['subcat'] == 'Medical':
		v = 10
	u.hostel_set.create(description=xs,userId=400,subcatId=v,incharge=incharge,hostelRoomNo=roomno) 
	u.save()

	from_gmail_user = 'grs.sem5@gmail.com'
	from_gmail_password = 'grssem5@123'
	#users = ['shruthi.ms16@iiits.in','parkhi.m16@iiits.in','mounika.c16@iiits.in','sreepragna.v16@iiits.in','sowmyavasuki.j16@iiits.in']
	user = ys
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(from_gmail_user, from_gmail_password)
	print("logged in")
	msg = MIMEMultipart()
	msg['From'] = from_gmail_user
	msg['To'] = user
	msg['Subject'] = "GRS Notification"
	body = "Complaint filed by: " + user + ", description: " + xs
	msg.attach(MIMEText(body, 'plain'))
	text = msg.as_string()
	server.sendmail(from_gmail_user, user, text)
	server.quit()

	template = loader.get_template('complaint/hostel_register.html')
	
	Xs= Hostel.objects.get(description=xs)
	m = LoggedInUser.objects.all()[0].userId
	u = User.objects.get(userRollNumber=m)
	uname = u.login_set.all()[0].userName
	context = {
		"success":'Thanks for Submission.',
		'list': Xs,
		"uname" : uname
	}
	return HttpResponse(template.render(context,request))

#Others reg'n confirmation
def others_confirm(request):
	m = LoggedInUser.objects.all()[0].userId
	u = User.objects.get(userRollNumber=m)
	xs = request.POST['description']
	ys = u.UserMailId
	u.others_set.create(description=xs,userId=400) 
	u.save()

	from_gmail_user = 'grs.sem5@gmail.com'
	from_gmail_password = 'grssem5@123'
	#users = ['shruthi.ms16@iiits.in','parkhi.m16@iiits.in','mounika.c16@iiits.in','sreepragna.v16@iiits.in','sowmyavasuki.j16@iiits.in']
	user = ys
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(from_gmail_user, from_gmail_password)
	print("logged in")
	msg = MIMEMultipart()
	msg['From'] = from_gmail_user
	msg['To'] = user
	msg['Subject'] = "GRS Notification"
	body = "Complaint filed by: " + user + ", description: " + xs
	msg.attach(MIMEText(body, 'plain'))
	text = msg.as_string()
	server.sendmail(from_gmail_user, user, text)
	server.quit()

	template = loader.get_template('complaint/others_register.html')
	
	Xs= Others.objects.get(description=xs)
	m = LoggedInUser.objects.all()[0].userId
	u = User.objects.get(userRollNumber=m)
	uname = u.login_set.all()[0].userName
	context = {
		"success":'Thanks for Submission.',
		'list': Xs,
		"uname" : uname
	}
	return HttpResponse(template.render(context,request))

'''
def academics(request):
	template = loader.get_template("complaint/academics.html")
	P = Academics.objects.all()[Academics.objects.count()-5:][::-1]
	context = {
	'display': P
	}
	return HttpResponse(template.render(context,request))
def sports(request):
	template = loader.get_template("complaint/sports.html")
	P = Sports.objects.all()[Sports.objects.count()-2:][::-1]
	context = {
	'display': P
	}
	return HttpResponse(template.render(context,request))
def events(request):
	template = loader.get_template("complaint/events.html")
	P = Events.objects.all()[Events.objects.count()-5:][::-1]
	context = {
	'display': P
	}
	return HttpResponse(template.render(context,request))
def others(request):
	template = loader.get_template("complaint/others.html")
	P = Others.objects.all()[Others.objects.count()-5:][::-1]
	context = {
	'display': P
	}
	return HttpResponse(template.render(context,request))
def hostel(request):
	template = loader.get_template("complaint/hostel.html")
	P = Hostel.objects.all()[Hostel.objects.count()-5:][::-1]
	context = {
	'display': P
	}
	return HttpResponse(template.render(context,request))
'''
