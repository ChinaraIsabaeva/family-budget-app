# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.db.models import Sum
from django.views.generic import UpdateView, CreateView

from mybudget.lib import disposable_income
from .models import Envelopes
from .forms import EnvelopesForm, EnvelopeSelectForm
from mybudget.apps.general.models import Incomes


def all_envelopes(request):
    envelopes = Envelopes.objects.all().order_by('name', 'cash')
    income = Incomes.objects.all().aggregate(total=Sum('amount'))
    available_amount = disposable_income()
    if income['total'] is None:
        income_total = 0
    else:
        income_total = income['total']
    return render(request, 'envelopes/envelopes.html',
                  {'envelopes': envelopes, 'income': income_total, 'available_amount': available_amount})


class EnvelopeCreate(CreateView):
    model = Envelopes
    template_name = 'envelopes/envelope_create.html'
    form_class = EnvelopesForm

    def post(self, request):
        form = EnvelopesForm(request.POST or None, initial={'account': '1'})
        if form.is_valid():
            form.save()
            return redirect(reverse('envelopes:all'))
        return render(request, 'envelopes/envelope_create.html', {'form': form})


class EnvelopeUpdate(UpdateView):
    model = Envelopes
    template_name = 'envelopes/envelope_update.html'
    form_class = EnvelopesForm

    def post(self, request, pk):
        envelope = Envelopes.objects.get(pk=pk)
        form = EnvelopesForm(request.POST or None, instance=envelope)
        if form.is_valid():
            envelope.save()
            return redirect(reverse('envelopes:all'))
        else:
            message = "Envelope didn't update, some problem occurred"
            return redirect('/envelopes/', message=message)


def envelope_select(request):
    form = EnvelopeSelectForm(request.POST or None)
    if form.is_valid():
        envelope = form.cleaned_data['envelope'].name
        return redirect(reverse('expenses:filtered_expenses', args=(envelope, )))
