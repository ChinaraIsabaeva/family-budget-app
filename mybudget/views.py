from django.shortcuts import render, redirect

from apps.budget.forms import ExpensesForm
from apps.budget.models import Envelopes


def home(request):
    form = ExpensesForm(request.POST or None)
    envelopes = Envelopes.objects.all()
    if form.is_valid():
        form.save()
        return redirect('/')
    else:
        form = ExpensesForm()
    return render(request, 'home.html', {'form': form, 'envelopes': envelopes})





