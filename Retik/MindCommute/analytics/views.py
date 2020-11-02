from django.shortcuts import render
from .models import Journal
from django.contrib.auth.mixins import LoginRequiredMixin

# Generic Class Views
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView

class CreateJournal(LoginRequiredMixin, CreateView):
    model = Journal
    fields = ['headline','content', 'author']
    success_url = '/analytics/journal'

class JournalList(LoginRequiredMixin, ListView):
    model = Journal
    ordering = ['-created','-modified']

class JournalDetail(LoginRequiredMixin, DetailView):
    model = Journal
