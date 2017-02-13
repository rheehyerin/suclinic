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

    # botox #
    url(r'^botox/$', views.botox, name="botox"),
    url(r'^filler/$', views.filler, name="filler"),

    # petit #
    url(r'^darkcircle/$', views.darkcircle, name="darkcircle"),
    url(r'^dermotoxin/$', views.dermotoxin, name="dermotoxin"),
    url(r'^highnose/$', views.highnose, name="highnose"),
    url(r'^kotppol/$', views.kotppol, name="kotppol"),
    url(r'^witch/$', views.witch, name="witch"),

    # contour #
    url(r'^bigeyes/$', views.bigeyes, name="bigeyes"),
    url(r'^contour/$', views.contour, name="contour"),
    url(r'^doublero/$', views.doublero, name="doublero"),
    url(r'^thread/$', views.thread, name="thread"),

    # pimple #
    url(r'^pimple/$', views.pimple, name="pimple"),

    # obesity #
    url(r'^carboxy/$', views.carboxy, name="carboxy"),
    url(r'^cinderella/$', views.cinderella, name="cinderella"),
    url(r'^coolshaping/$', views.coolshaping, name="coolshaping"),
    url(r'^highfrequency/$', views.highfrequency, name="highfrequency"),
    url(r'^hpl/$', views.hpl, name="hpl"),
    url(r'^mesotherapie/$', views.mesotherapie, name="mesotherapie"),
    url(r'^slim/$', views.slim, name="slim"),

    url(r'^map/$', views.map, name="map"),

    url(r'^$', views.main, name="main"),
]
