from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^blog/(?P<pk>\d+)/$', views.post, name='post'),
    url(r'^blog/$', views.blog, name='blog'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^cv/$', views.cv, name='cv'),
]
