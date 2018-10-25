# -*- coding: utf-8 -*-
from __future__ import unicode_literals



# Create your views here.
from django.shortcuts import render
from . models import *
# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
def index(request):
	template = loader.get_template("complaint/home.html")
	#x = academics.objects.all()
	context = {
	#	'list' : x
	}
	return HttpResponse(template.render(context,request))

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

def register(request):
	print('in function')
	x = request.POST['description']
	y = request.POST['email']
	p = Academics()
	p.description = x
	p.acadId = 300
	p.userId = 400
	p.incharge = 'qwerty'
	p.subcatId = 1
	print('before saving')
	p.save()
	print('after saving')
	'''from_gmail_user = 'scoutbotsem4@gmail.com'
	from_gmail_password = 'scoutbot@123'
	#users = ['shruthi.ms16@iiits.in','parkhi.m16@iiits.in','mounika.c16@iiits.in','sreepragna.v16@iiits.in','sowmyavasuki.j16@iiits.in']
	user = y 
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
	server.quit()'''
	template = loader.get_template('complaint/academics.html')
	X = Academics.objects.all()
	context = {
		"list" : X
	}
	return HttpResponse(template.render(context,request))


def aform(request):
	template = loader.get_template("complaint/acad_register.html")
	context = {

	}
	return HttpResponse(template.render(context,request))
def acad_confirm(request):
	x = request.POST['description']
	y = request.POST['email']
	p = Academics()
	p.description = x
	#p.acadId = 300
	p.userId = 400
	p.incharge = 'qwerty'
	if request.POST['subcat'] == 'Library':
		p.subcatId = 1
	if request.POST['subcat'] == 'Scholarship/Placement':
		p.subcatId = 2
	if request.POST['subcat'] == 'Course':
		p.subcatId = 3
	else:
		p.subcatId = 4
	p.save()

	from_gmail_user = 'grs.sem5@gmail.com'
	from_gmail_password = 'grssem5@123'
	#users = ['shruthi.ms16@iiits.in','parkhi.m16@iiits.in','mounika.c16@iiits.in','sreepragna.v16@iiits.in','sowmyavasuki.j16@iiits.in']
	user = y 
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
	
	X = Academics.objects.get(description=x)

	context = {
		"success":'Thanks for Submission.',
		'list': X

	}
	return HttpResponse(template.render(context,request))





def sform(request):
	template = loader.get_template("complaint/sport_register.html")
	context = {

	}
	return HttpResponse(template.render(context,request))

def sport_confirm(request):
	xs = request.POST['description']
	ys= request.POST['email']
	p1 = Sports()
	p1.description = xs
	#p.acadId = 300
	p1.userId = 400
	p1.sportname = request.POST['spname']
	if request.POST['subcat'] == 'Indoor':
		p1.subcatId = 5
	if request.POST['subcat'] == 'Outdoor':
		p1.subcatId = 6
	
	p1.save()

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

	template = loader.get_template('complaint/sport_register.html')
	
	Xs= Sports.objects.get(description=xs)

	context = {
		"success":'Thanks for Submission.',
		'list': Xs

	}
	return HttpResponse(template.render(context,request))