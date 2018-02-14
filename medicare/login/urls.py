'''
Created on Feb 11, 2018

@author: trupa7
'''
'''
Created on Feb 1, 2018

@author: trupa7
'''
from django.urls import path
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.views.generic.base import TemplateView
from django.conf import settings
from . import views
app_name="login"
urlpatterns = [
    path('', views.index, name='index'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^auth/$', views.auth_view, name='auth'),
]

