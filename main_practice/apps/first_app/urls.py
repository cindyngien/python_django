#  From inside apps/first_app/urls.py
from django.conf.urls import url
from . import views
#from wherever we're at, go and get those views, those views are our controllers

urlpatterns = [
url(r'^$', views.index)     # This line has changed!
]
