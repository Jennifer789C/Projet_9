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


class CritiqueForm(forms.ModelForm):
    CHOIX = [("0", "0"), ("1", "1"), ("2", "2"), ("3", "3"), ("4", "4"),
             ("5", "5")]
    note = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOIX)

    class Meta:
        model = models.Critique
        fields = ["entete", "note", "commentaire"]
