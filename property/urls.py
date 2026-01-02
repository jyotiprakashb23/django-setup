# property/urls.py
from django.urls import path
from .views import create_property,test

urlpatterns = [
    path('create/', create_property),
    path('test/', test),
    # path('list/', list_properties),
]
