from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login$', views.Login,name='login'),
    url(r'^register$', views.register,name='register'),
    url(r'^category$', views.Category,name='category'),
    url(r'^profile$', views.Profile,name='profile'),
    url(r'^requestOtp$', views.requestOtp,name='requestOtp'),
    url(r'^validateOtp$', views.validateOtp,name='validateOtp'),
]