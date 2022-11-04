from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from . import forms
from connexion import models

User = get_user_model()


@login_required
def flux(request):
    return render(request, "flux.html")


@login_required
def suivre_user(request):
    form = forms.AbonnementForm(instance=request.user)
    connecte = request.user
    if request.method == "POST":
        form = forms.AbonnementForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("abonnements")
    user_suivis = connecte.user_suivi.all()
    abonnes = connecte.suivi_par.all()
    context = {"form": form, "user_suivis": user_suivis, "abonnés": abonnes}
    return render(request, "abonnements.html", context=context)
