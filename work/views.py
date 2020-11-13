from django.http import HttpResponseRedirect
from django.shortcuts import render
from work.models import HoursInput
from work.forms import HoursInputForm
import psycopg2


def get_basic_workdata(request):
    title = None
    if request.method == 'POST':
        form = HoursInputForm(request.POST)
        if form.is_valid():
            form.save()
            # form.date = request.POST.get('date')
            # form.hours_number = request.POST.get('hours_number')
            # form.workplace = request.POST.get('workplace')
            # date = form.cleaned_data['date']
            # hours_number = form.cleaned_data['hours_number']
            # workplace = form.cleaned_data['workplace']
            return HttpResponseRedirect('/')
    else:
        form = HoursInputForm()

    return render(request, 'inputhours.html', {'form': form, 'title': title})

