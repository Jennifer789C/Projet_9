from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.conf import settings
from . import forms


def inscription_page(request):
    form = forms.InscriptionForm()
    if request.method == "POST":
        form = forms.InscriptionForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request, "inscription.html", {"form": form})
