# -*- coding: utf-8 -*-
# @Author: Charlie Gallentine
# @Date:   2018-11-23 12:01:38
# @Last Modified by:   Charlie Gallentine
# @Last Modified time: 2018-11-23 13:09:54
from django.urls import path, include
from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]