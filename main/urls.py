from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^whitening/$', views.whitening, name="whitening"),
    url(r'^laser/$', views.laser, name="laser"),
    url(r'^jade/$', views.jade, name="jade"),
    url(r'^targeting/$', views.targeting, name="targeting"),
    url(r'^$', views.main, name="main"),
]
