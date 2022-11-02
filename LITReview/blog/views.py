from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def flux(request):
    return render(request, "flux.html")


@login_required
def suivre_user(request):
    return render(request, "abonnements.html")
