from django.shortcuts import render, redirect

from .forms import EnvelopesForm
from .models import RegularMonthlyExpenses, Envelopes


def budget(request):
    form = EnvelopesForm(request.POST or None)
    regular_expenses = RegularMonthlyExpenses.objects.all()
    envelopes = Envelopes.objects.all()
    if form.is_valid():
        form.save()
        return redirect('/budget')
    else:
        form = EnvelopesForm()
    return render(request, 'dashboard.html',
                  {'form': form,
                  'regexpenses': regular_expenses,
                  'envelopes': envelopes})



