from django.shortcuts import render, redirect, get_object_or_404
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
    if request.method == "POST":
        form = forms.AbonnementForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["utilisateur"]
            user_suivi = get_object_or_404(User, username=username)
            models.Abonnement.objects.create(user=request.user,
                                             user_suivi=user_suivi)
            return redirect("abonnements")
    connecte = request.user
    abonnements = models.Abonnement.objects.all()
    abonnes = connecte.suivi_par.all()
    context = {"form": form, "abonnements": abonnements, "abonnés": abonnes}
    return render(request, "abonnements.html", context=context)


@login_required
def desabonner(request, abonnement_id):
    desabonnement = forms.DesabonnementForm()
    abonnement = get_object_or_404(models.Abonnement, id=abonnement_id)
    if request.method == "POST":
        desabonnement = forms.DesabonnementForm(request.POST)
        if desabonnement.is_valid():
            abonnement.delete()
            return redirect("abonnements")
    context = {"désabonnement": desabonnement, "abonnement": abonnement}
    return render(request, "désabonnement.html", context=context)
