from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^notice/(?P<pk>\d+)/$', views.NoticeDetail.as_view(), name="notice_detail"),
    url(r'^notice/delete/(?P<pk>\d+)/$', views.NoticeDelete.as_view(), name="notice_delete"),
    url(r'^notice/hide/(?P<pk>\d+)/$', views.NoticeHide.as_view(), name="notice_hide"),
    url(r'^notice/edit/(?P<pk>\d+)/$', views.NoticeUpdate.as_view(), name="notice_update"),
    url(r'^notice/new/$', views.NoticeCreate.as_view(), name="notice_create"),
    url(r'^notice/$', views.NoticeList.as_view(), name="notice_list"),

    url(r'^review/(?P<pk>\d+)/$', views.ReviewDetail.as_view(), name="review_detail"),
    url(r'^review/delete/(?P<pk>\d+)/$', views.ReviewDelete.as_view(), name="review_delete"),
    url(r'^review/hide/(?P<pk>\d+)/$', views.ReviewHide.as_view(), name="review_hide"),
    url(r'^review/edit/(?P<pk>\d+)/$', views.ReviewUpdate.as_view(), name="review_update"),
    url(r'^review/new/$', views.ReviewCreate.as_view(), name="review_create"),
    url(r'^review/$', views.ReviewList.as_view(), name="review_list"),

    url(r'^beforeafter/(?P<pk>\d+)/$', views.BeforeAfterDetail.as_view(), name="beforeafter_detail"),
    url(r'^beforeafter/delete/(?P<pk>\d+)/$', views.BeforeAfterDelete.as_view(), name="beforeafter_delete"),
    url(r'^beforeafter/hide/(?P<pk>\d+)/$', views.BeforeAfterHide.as_view(), name="beforeafter_hide"),
    url(r'^beforeafter/edit/(?P<pk>\d+)/$', views.BeforeAfterUpdate.as_view(), name="beforeafter_update"),
    url(r'^beforeafter/new/$', views.BeforeAfterCreate.as_view(), name="beforeafter_create"),
    url(r'^beforeafter/$', views.BeforeAfterList.as_view(), name="beforeafter_list"),

    url(r'^counsel/(?P<pk>\d+)/$', views.CounselDetail.as_view(), name="counsel_detail"),
    url(r'^counsel/delete/(?P<pk>\d+)/$', views.CounselDelete.as_view(), name="counsel_delete"),
    url(r'^counsel/hide/(?P<pk>\d+)/$', views.CounselHide.as_view(), name="counsel_hide"),
    url(r'^counsel/edit/(?P<pk>\d+)/$', views.CounselUpdate.as_view(), name="counsel_update"),
    url(r'^counsel/new/$', views.CounselCreate.as_view(), name="counsel_create"),
    url(r'^counsel/$', views.CounselList.as_view(), name="counsel_list"),
]
