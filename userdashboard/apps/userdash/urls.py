from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='dashindex'),
    url(r'^signin$', views.signin, name='dashsignin'),
    url(r'^register$', views.register, name='dashregister'),
]
