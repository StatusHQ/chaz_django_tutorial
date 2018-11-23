# -*- coding: utf-8 -*-
# @Author: Charlie Gallentine
# @Date:   2018-11-23 12:01:38
# @Last Modified by:   Charlie Gallentine
# @Last Modified time: 2018-11-23 13:00:40
from django.urls import path, include
from . import views

app_name = 'polls'

urlpatterns = [
	# Create map from view to URL
	path('', views.index, name='index'),
	path('<int:question_id>/', views.detail, name='detail'),
	path('<int:question_id>/results/', views.results, name='results'),
	path('<int:question_id>/vote/', views.vote, name='vote'),
]