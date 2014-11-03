# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',
    url(r'^(?P<id>\d+)/(?P<slug>[\w\d-]+)$', views.MyAccount.as_view(), name='my_account'),
)
