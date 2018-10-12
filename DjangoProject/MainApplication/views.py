from django.shortcuts import render
from . models import *
# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt


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
