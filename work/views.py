from django.http import HttpResponseRedirect
from django.shortcuts import render
from work.forms import *
from django.contrib.auth.decorators import login_required


@login_required
def get_basic_workdata(request):
    title = "Godziny"
    if request.method == 'POST':
        form = HoursInputForm(request.POST)
        if form.is_valid():
            fs = form.save(commit=False)
            fs.user = request.user
            fs.save()
            return HttpResponseRedirect('/')
    else:
        form = HoursInputForm()

    return render(request, 'inputhours.html', {'form': form, 'title': title})


@login_required
def addworkplace_view(request):
    title = "Prace"
    if request.method == 'POST':
        form = WorkplaceInputForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/work/workplaces/')
    else:
        form = WorkplaceInputForm()

    return render(request, 'addworkplace.html', {'form': form, 'title': title})


@login_required
def show_workplaces(request):
    title = "Prace"
    workplaces = WorkplaceInput.objects
    return render(request, 'workplaces.html', {'workplaces': workplaces, 'title': title})