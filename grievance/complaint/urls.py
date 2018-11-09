from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index,name='index'),
	url(r'^login$', views.Login,name='login'),
	url(r'^dashboard/(?P<token>.+)$', views.dashboard,name='dashboard'),
	url(r'^category$', views.Category,name='category'),
	url(r'^category2$', views.Category2,name='category2'),
	url(r'^category3$', views.Category3,name='category3'),
	url(r'^category4$', views.Category4,name='category4'),
	url(r'^category5$', views.Category5,name='category5'),
	url(r'^aform$', views.aform,name='aform'),
	url(r'^sform$', views.sform,name='sform'),
	url(r'^eform$', views.eform,name='eform'),
	url(r'^hform$', views.hform,name='hform'),
	url(r'^oform$', views.oform,name='oform'),
	url(r'^acadconfirm$', views.acad_confirm,name='acad_confirm'),
	url(r'^sportconfirm$', views.sport_confirm,name='sport_confirm'),
	url(r'^eventconfirm$', views.event_confirm,name='event_confirm'),
	url(r'^hostelconfirm$', views.hostel_confirm,name='hostel_confirm'),
	url(r'^othersconfirm$', views.others_confirm,name='others_confirm'),
	url(r'^profile$', views.Profile,name='profile'),
	url(r'^requestOtp$', views.requestOtp,name='requestOtp'),
    url(r'^validateOtp$', views.validateOtp,name='validateOtp'),
    url(r'^incharge$', views.incharge,name='incharge'),
    url(r'^listcomp$', views.listcomp,name='listcomp'),


	url(r'^disppoll$', views.disppoll,name='disppoll'),
	url(r'^question$', views.poll_question,name='poll_question'),
	url(r'^look$', views.look,name='look'),

	url(r'^showpoll/(?P<pk>\d+)/$', views.show_poll,name='show_poll'),
	url(r'^vote/(?P<pk>\d+)/$', views.vote,name='vote'),

	#url(r'^academics$', views.academics,name='academics'),
	#url(r'^others$', views.others,name='others'),
	#url(r'^events$', views.events,name='events'),
	#url(r'^sports$', views.sports,name='sports'),
	#url(r'^hostel$', views.hostel,name='hostel'),
    #url(r'^register$', views.register,name='register'),
]