from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from . import forms, models

User = get_user_model()


@login_required
def flux(request):
    tickets = models.Ticket.objects.all()
    critiques = models.Critique.objects.all()
    context = {"tickets": tickets, "critiques": critiques}
    return render(request, "flux.html", context=context)


@login_required
def posts(request):
    tickets = models.Ticket.objects.filter(user=request.user)
    critiques = models.Critique.objects.filter(user=request.user)
    context = {"tickets": tickets, "critiques": critiques}
    return render(request, "posts.html", context=context)


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


@login_required
def modifier_ticket(request, ticket_id):
    ticket = get_object_or_404(models.Ticket, id=ticket_id)
    modifier_form = forms.TicketForm(instance=ticket)
    supprimer_form = forms.SupprimerTicketForm()
    if request.method == "POST":
        if "modifier_ticket" in request.POST:
            modifier_form = forms.TicketForm(request.POST, request.FILES,
                                             instance=ticket)
            if modifier_form.is_valid():
                modifier_form.save()
                return redirect("posts")
        if "supprimer_ticket" in request.POST:
            supprimer_form = forms.SupprimerTicketForm(request.POST)
            if supprimer_form.is_valid():
                ticket.delete()
                return redirect("posts")
    context = {"modifier_form": modifier_form,
               "supprimer_form": supprimer_form}
    return render(request, "modifier_ticket.html", context=context)


@login_required
def creer_critique_et_ticket(request):
    ticket_form = forms.TicketForm()
    critique_form = forms.CritiqueForm()
    if request.method == "POST":
        ticket_form = forms.TicketForm(request.POST, request.FILES)
        critique_form = forms.CritiqueForm(request.POST)
        if all([ticket_form.is_valid(), critique_form.is_valid()]):
            ticket = ticket_form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            critique = critique_form.save(commit=False)
            critique.user = request.user
            critique.ticket = ticket
            critique.save()
            return redirect("flux")
    context = {"ticket_form": ticket_form, "critique_form": critique_form}
    return render(request, "creer_critique.html", context=context)
