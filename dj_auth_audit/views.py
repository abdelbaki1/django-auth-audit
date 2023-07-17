# -*- coding: utf-8 -*-
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    UpdateView,
    ListView
)

from .models import (
	AuthLogEntry,
)


class AuthLogEntryCreateView(CreateView):

    model = AuthLogEntry


class AuthLogEntryDeleteView(DeleteView):

    model = AuthLogEntry


class AuthLogEntryDetailView(DetailView):

    model = AuthLogEntry


class AuthLogEntryUpdateView(UpdateView):

    model = AuthLogEntry


class AuthLogEntryListView(ListView):

    model = AuthLogEntry

