from django.conf.urls import url
from . import views
from insta.views import Index

urlpatterns=[
    url('', Index.as_view(), name="Index"),
]