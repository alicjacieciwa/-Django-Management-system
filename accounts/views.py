from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


@login_required
def sign_up(request):
    title = "Rejestracja"
    form = UserCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            return redirect("/")
    return render(request, 'registration/signup.html', {"form": form, 'title': title})


def logout_view(request):
    logout(request)
    return redirect('/accounts/login')

