# -*- coding: utf-8 -*-

from django.urls import path
from stackerui import views

urlpatterns = [
    path('', views.frontpage, name='frontpage'),
]