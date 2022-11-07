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
            username = form.cleaned_data["utilisateur"]
            user_suivi = User.objects.get(username=username)
            models.Abonnement.objects.create(user=request.user,
                                             user_suivi=user_suivi)
            return redirect("abonnements")
    user_suivis = connecte.qui_suit.all()
    abonnes = connecte.suivi_par.all()
    context = {"form": form, "user_suivis": user_suivis, "abonnés": abonnes}
    return render(request, "abonnements.html", context=context)
