from django.conf.urls import url

from . import views
urlpatterns = [
    url(r'^$', views.index, name = 'loginreg_index'),
    url(r'^register$', views.register, name = 'regregister'),
    url(r'^login$', views.login, name = 'reglogin'),
    url(r'^success$', views.success, name = 'loginreg_success')
]
