from django.conf.urls import url
from django.contrib.auth.views import login, logout

urlpatterns=[
    url(r'^login/$', login, name="login"),
]
