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
	template = loader.get_template("MainApplication/try.html")
	x = Academics.objects.all()
	context = {
		'list' : x
	}
	return HttpResponse(template.render(context,request))

def Category(request):
	template = loader.get_template("MainApplication/category.html")
	X = Academics.objects.all()
	context = {
		"list" : X
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

			#x.farmerlogin_set.create(farmerid=x.farmerid,login=1,time=timezone.now())
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
def register(request):
	x = request.POST['description']
	y = request.POST['email']
	p = Academics()
	p.description = x
	p.acadId = 300
	p.userId = 400
	p.incharge = request.POST['incharge']
	p.subcatId = request.POST['subcat']
	p.save()
	from_gmail_user = 'scoutbotsem4@gmail.com'
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
	server.quit()
	template = loader.get_template('MainApplication/category.html')
	X = Academics.objects.all()
	context = {
		"list" : X
	}
	return HttpResponse(template.render(context,request))
