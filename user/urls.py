from django.contrib import admin
from django.urls import path
# from home.views import * 
from user.views import *

urlpatterns = [
    path('', home, name='home'),
    path('create_user/', create_user, name='create_user'),
    path('all_users/', get_all_users, name='get_all_users'),
]