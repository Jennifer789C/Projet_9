from django import forms


class AbonnementForm(forms.Form):
    utilisateur = forms.CharField(max_length=150)


class DesabonnementForm(forms.Form):
    desabonner = forms.BooleanField(widget=forms.HiddenInput, initial=True)
