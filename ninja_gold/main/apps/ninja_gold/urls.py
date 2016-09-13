from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^processmoney$', views.processmoney),
    url(r'^clear$', views.clear)
]
