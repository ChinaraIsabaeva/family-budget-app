# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import UpdateView, CreateView, ListView

from mybudget.envelopes.forms import EnvelopesForm, EnvelopeSelectForm
from mybudget.envelopes.models import Envelopes


class EnvelopeListView(ListView):
    model = Envelopes
    template_name = 'envelopes/envelopes.html'
    context_object_name = 'envelopes'


class EnvelopeCreate(CreateView):
    model = Envelopes
    template_name = 'envelopes/envelope_create.html'
    form_class = EnvelopesForm

    def get_success_url(self):
        return reverse('envelopes:all')


class EnvelopeUpdate(UpdateView):
    model = Envelopes
    template_name = 'envelopes/envelope_update.html'
    form_class = EnvelopesForm

    def get_success_url(self):
        return reverse('envelopes:all')


def envelope_select(request):
    form = EnvelopeSelectForm(request.POST or None)
    if form.is_valid():
        envelope = form.cleaned_data['envelope'].name
        return redirect(reverse('expenses:filtered_expenses', args=(envelope, )))
