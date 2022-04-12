from django.urls import re_path
from . import views


urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^blog/(?P<pk>\d+)/$', views.post, name='post'),
    re_path(r'^blog/$', views.blog, name='blog'),
    re_path(r'^contact/$', views.contact, name='contact'),
    re_path(r'^cv/$', views.cv, name='cv'),
]
