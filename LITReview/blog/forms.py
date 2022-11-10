from django import forms
from . import models


class TicketForm(forms.ModelForm):
    modifier_ticket = forms.BooleanField(widget=forms.HiddenInput,
                                         initial=True)

    class Meta:
        model = models.Ticket
        fields = ["titre", "description", "image"]


class SupprimerTicketForm(forms.Form):
    supprimer_ticket = forms.BooleanField(widget=forms.HiddenInput,
                                          initial=True)
