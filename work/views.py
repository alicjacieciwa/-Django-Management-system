from django.http import HttpResponseRedirect
from django.shortcuts import render
from work.forms import HoursInputForm
from django.contrib.auth.decorators import login_required

#
# @login_required
# def index(request):
#     return render(request,'registration/login.html')

@login_required
def get_basic_workdata(request):
    title = "Godziny"
    if request.method == 'POST':
        form = HoursInputForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = HoursInputForm()

    return render(request, 'inputhours.html', {'form': form, 'title': title})

