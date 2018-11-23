# -*- coding: utf-8 -*-
# @Author: Charlie Gallentine
# @Date:   2018-11-23 12:01:38
# @Last Modified by:   Charlie Gallentine
# @Last Modified time: 2018-11-23 12:06:27
from django.urls import path, include
from . import views

urlpatterns = [
	# Create map from view to URL
	path('', views.index, name='index'),
]