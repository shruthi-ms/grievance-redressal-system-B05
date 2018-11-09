# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
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
import requests
import simplejson as json

def index(request):
	template = loader.get_template("complaint/login.html")
	#x = academics.objects.all()
	context = {
	#	'list' : x
	}
	return HttpResponse(template.render(context,request))
def dashboard(request,token):
	details = auth_api(token)
	print("yes!!!")
	print(details)
	name = details['student'][0]['Student_First_Name']
	template = loader.get_template("complaint/home.html")
	#x = academics.objects.all()
	context = {
		'list' :name,
	}
	return HttpResponse(template.render(context,request))
def auth_api(token):
    url = ' https://10.0.80.133:3000/oauth/getDetails'
    Payload = {'token':token, 'secret':"2e9af1ae7fda17d3d74a125b39348b612f046a6ed5d6b65e1cd01fdeae32da15bdc54b02923b24d7acb3b5ddb995b3a0263cd99f4b021979e40abb1bb2fadff1"}
    s = requests.post(url,Payload)
    details = json.loads(s.content)
    return details
def Login(request):
	if request.method=='POST':
		#Check if the username and password are valid
		try:
			x = login.objects.get(userName=request.POST['email'])
		except(KeyError, login.DoesNotExist):
			template = loader.get_template('complaint/login.html')
			context = {
					'pass':"Invalid Username !",
				}
			return HttpResponse(template.render(context,request))
		if request.POST['pass'] != x.paword:
			template = loader.get_template('complaint/login.html')
			context = {
					'mess':"Incorrect password!",
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

#Incharge
def incharge(request):
	template = loader.get_template("complaint/incharge.html")
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

#Academics
def Category(request):
	template = loader.get_template("complaint/academics.html")
	#get the id of current logged in user
	m = LoggedInUser.objects.all()[0].userId
	u = User.objects.get(userRollNumber=m)
	X = u.academics_set.all()
	#Y = Academics.objects.all()
	#get the username
	Y = Academics.objects.all()[Academics.objects.count()-2:][::-1]
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
	#Y = Sports.objects.all()
	Y = Sports.objects.all()[Sports.objects.count()-2:][::-1]
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
	#Y = Events.objects.all()
	Y = Events.objects.all()[Events.objects.count()-2:][::-1]
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
	#Y = Hostel.objects.all()
	Y = Hostel.objects.all()[Hostel.objects.count()-2:][::-1]
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
	#Y = Others.objects.all()
	Y = Others.objects.all()[Others.objects.count()-2:][::-1]
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
		v1 = "Salman Khan"
	if request.POST['subcat'] == 'Scholarship/Placement':
		v = 2
		v1 = "Sukanya"
	if request.POST['subcat'] == 'Course':
		v = 3
		v1 = "Siribabu"
	else:
		v = 4
		v1 = "Sai Krishna"
	u.academics_set.create(description=x,userId=400,incharge=v1,subcatId=v) 
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
	#S = table_complaint.objects.get(userId=m)
	V = Academics.objects.get(description=x)
	context = {
		"success" : 'Thanks for submission',
		"confirm" : V,
		"list" : X,
		"AllList" : Y
		#"comlist":S
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
	if request.POST['subcat'] == 'Academic':
		vv = 7
	if request.POST['subcat'] == 'Non-academic':
		vv = 8

	u.events_set.create(description=xs,userId=400,eventname=request.POST['ename'],subcatId=vv,nature=nature) 
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
	incharge = request.POST.get('incharge', False)
	roomno = request.POST['roomno']
	ys = u.UserMailId
	if request.POST['subcat'] == 'Accomodation':
		v = 9
	if request.POST['subcat'] == 'Mess':
		v = 10
	if request.POST['subcat'] == 'Transport':
		v = 11
	if request.POST['subcat'] == 'Medical':
		v = 12
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

def poll_question(request):
	if request.method=="POST":
		q = request.POST.get('ques', False)
		x1 = table_complaint.objects.get(Compid=request.POST.get('cid', False))
		if x1.Compid != '':
			p = Questions()
			p.question = q
			p.ComplaintId = request.POST.get('cid', False)
			p.active_till = request.POST.get('val_time', False)
			p.pub_date = datetime.datetime.now()
			p.save()
			'''x1.qaId = Questions().objects.get(question=q).questionId
			x1.poll = "yes"
			x1.save()'''
		u = Questions.objects.get(question=q)
	for i in range(0,4):
		if request.POST.get('Option' + str(i+1),False) != '':
			print("yes")
			b = request.POST['Option' + str(i+1)]
			u.choice_set.create(qid=u.questionId,ChoiceOption=b,votes=0) 
			u.save()
			'''a = Choice()
			a.qid = 
			a.ChoiceOption = 
			a.save()'''

	template = loader.get_template('complaint/question.html')
	

	context = {
		'success': 'Poll Registered successfully'

	}
	return HttpResponse(template.render(context,request))

def look(request):
	template = loader.get_template("complaint/polls.html")
	#X = table_complaint.objects.all()
	m = LoggedInUser.objects.all()[0].userId
	u = User.objects.get(userRollNumber=m)
	uname = u.login_set.all()[0].userName
	que=Questions.objects.all()
	context = {
		'uname':uname,
		'list':que

	}
	return HttpResponse(template.render(context,request))

def show_poll(request,pk):
	
	template = loader.get_template("complaint/vote.html")
	
	print(pk)
	que=Questions.objects.get(questionId=pk)
	q1=que.choice_set.all()
	#selected = que.choice_set.get(ChoiceOption=request.POST.get('choice',False))
	#selected.votes +=1
	#selected.save()
	context = {
		'qid' : pk,
		'total':q1,
		'list':que

	}
	return HttpResponse(template.render(context,request))

#voting for a poll
def vote(request,pk):
	
	template = loader.get_template("complaint/vote.html")
	#print("ghvxhgvg")
	print(pk)
	que=Questions.objects.get(questionId=pk)
	m=request.POST.get('option',False)
	print(m)
	selected = que.choice_set.get(ChoiceOption=m)
	selected.votes +=1
	selected.save()
	context = {
		'qa':que,
		'success': 'Recorded'
	}
	return HttpResponse(template.render(context,request))

#displaying a poll options
def disppoll(request):
	template = loader.get_template("complaint/question.html")
	context = {

	}
	return HttpResponse(template.render(context,request))


def listcomp(request):
	template = loader.get_template('complaint/usecomp.html')
	m = LoggedInUser.objects.all()[0].userId
	U = table_complaint.objects.all()
	print(U)
	u = User.objects.get(userRollNumber=m)
	uname = u.login_set.all()[0].userName
	que=Questions.objects.all()
	context = {
		"m" : m,
		'uname':uname,
		'list':que

	}
	#V = Academics.objects.get(description=x)
	return HttpResponse(template.render(context,request))

