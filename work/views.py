from django.http import HttpResponseRedirect
from django.shortcuts import render
from work.forms import HoursInputForm


def get_basic_workdata(request):
    title = 'Rejestracja'
    if request.method == 'POST':
        form = HoursInputForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/home/')
    else:
        form = HoursInputForm()

    return render(request, 'inputhours.html', {'form': form, 'title': title})

