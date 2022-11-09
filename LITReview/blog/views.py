from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from . import forms, models

User = get_user_model()


@login_required
def flux(request):
    tickets = models.Ticket.objects.all()
    context = {"tickets": tickets}
    return render(request, "flux.html", context=context)


@login_required
def creer_ticket(request):
    form = forms.TicketForm()
    if request.method == "POST":
        form = forms.TicketForm(request.POST, request.FILES)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            return redirect("flux")
    context = {"form": form}
    return render(request, "creer_ticket.html", context=context)
