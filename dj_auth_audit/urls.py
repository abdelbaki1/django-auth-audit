# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.views.generic import TemplateView

from . import views


app_name = 'dj_auth_audit'
urlpatterns = [
    url(
        regex="^AuthLogEntry/~create/$",
        view=views.AuthLogEntryCreateView.as_view(),
        name='AuthLogEntry_create',
    ),
    url(
        regex="^AuthLogEntry/(?P<pk>\d+)/~delete/$",
        view=views.AuthLogEntryDeleteView.as_view(),
        name='AuthLogEntry_delete',
    ),
    url(
        regex="^AuthLogEntry/(?P<pk>\d+)/$",
        view=views.AuthLogEntryDetailView.as_view(),
        name='AuthLogEntry_detail',
    ),
    url(
        regex="^AuthLogEntry/(?P<pk>\d+)/~update/$",
        view=views.AuthLogEntryUpdateView.as_view(),
        name='AuthLogEntry_update',
    ),
    url(
        regex="^AuthLogEntry/$",
        view=views.AuthLogEntryListView.as_view(),
        name='AuthLogEntry_list',
    ),
	]
