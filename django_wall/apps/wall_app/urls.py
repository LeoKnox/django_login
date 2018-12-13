from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^welcome$', views.welcome),
    url(r'^login$', views.login),
    url(r'^show$', views.show),
    url(r'^delete$', views.delete),
]