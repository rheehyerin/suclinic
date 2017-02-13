from django.conf.urls import url
from . import views

urlpatterns = [
    # whitening #
    url(r'^whitening/$', views.whitening, name="whitening"),
    url(r'^laser/$', views.laser, name="laser"),
    url(r'^jade/$', views.jade, name="jade"),
    url(r'^targeting/$', views.targeting, name="targeting"),

    # peeling #
    url(r'^aqua/$', views.aqua, name="aqua"),
    url(r'^celebrity/$', views.celebrity, name="celebrity"),
    url(r'^latte/$', views.latte, name="latte"),
    url(r'^spectra/$', views.spectra, name="spectra"),

    # scar #
    url(r'^legato/$', views.legato, name="legato"),
    url(r'^prp/$', views.prp, name="prp"),
    url(r'^tera/$', views.tera, name="tera"),

    url(r'^$', views.main, name="main"),
]
