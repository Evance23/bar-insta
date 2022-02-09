from django.conf.urls import url
from django.urls import path 
from . import views
# from insta.views import Index

urlpatterns=[
    path('', views.index, name="index"), 
]