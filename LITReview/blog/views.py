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
    form = forms.AbonnementForm()
    connecte = request.user
    if request.method == "POST":
        form = forms.AbonnementForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["user_suivi"]
            user_id = User.objects.get(username=username)
            user_suivi = models.Abonnement.user_suivi.create(user_suivi_id=user_id)
            connecte.user_suivi.add(user_suivi)
            return redirect("abonnements")
    user_suivis = connecte.user_suivi.all()
    abonnes = connecte.suivi_par.all()
    context = {"form": form, "user_suivis": user_suivis, "abonnés": abonnes}
    return render(request, "abonnements.html", context=context)
