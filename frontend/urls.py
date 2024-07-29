from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('',index,name="home"),
    path('contect/',contect,name="contect"),
    path('login/',login,name="login"),
]