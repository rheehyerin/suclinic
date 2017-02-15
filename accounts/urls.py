from django.conf.urls import url
from django.contrib.auth.views import login, logout
from . import views

urlpatterns=[
    url(r'^login/$', views.login, name = 'login'),
    url(r'^signup/$', views.signup, name = 'signup'),
    url(r'^logout/$', logout, {
        'next_page' : 'main:main'
        }, name="logout"),
]
