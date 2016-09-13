from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^create$', views.create, name = "add_course"),
    url(r'^destroy/(?P<course_id>\d+)$', views.destroy, name = "destroy"),
    url(r'^delete$', views.delete, name = "delete")
]
