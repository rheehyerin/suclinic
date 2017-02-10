from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^whitening/$', views.whitening, name="main"),
    url(r'^$', views.main, name="main"),
]
