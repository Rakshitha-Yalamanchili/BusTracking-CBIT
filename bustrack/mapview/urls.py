"""bustrack URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include,re_path
from . import views

urlpatterns = [
	path('home/',views.index,name='index'),
    #/homepage/
	path('homepage/',views.homepage,name='homepage'),
    #/home/Bus-67/
    re_path(r'^home/Bus-(?P<bno>[0-9]+)/$', views.detail, name='detail'),
    #/home/alerts
    path('home/alerts',views.alerts,name='alerts'),
	#/info/<bno>
    path('info/<bno>',views.info,name='info'),
    
]
