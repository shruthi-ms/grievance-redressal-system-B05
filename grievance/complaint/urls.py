from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index,name='index'),
	url(r'^aform$', views.aform,name='aform'),
	url(r'^sform$', views.sform,name='sform'),
	url(r'^acadconfirm$', views.acad_confirm,name='acad_confirm'),
	url(r'^sportconfirm$', views.sport_confirm,name='sport_confirm'),


	url(r'^academics$', views.academics,name='academics'),
	url(r'^others$', views.others,name='others'),
	url(r'^events$', views.events,name='events'),
	url(r'^sports$', views.sports,name='sports'),
	url(r'^hostel$', views.hostel,name='hostel'),

    url(r'^register$', views.register,name='register'),
]