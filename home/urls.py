"""
Created by Framework
This file is where you can set the urls to your views.
Modified by: Jorge Nino
Date: 15/03/20
"""
# Import libraries needed
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'),
]
