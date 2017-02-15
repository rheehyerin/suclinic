from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^notice/$', views.NoticeList.as_view(), name='notice_list'),
]
