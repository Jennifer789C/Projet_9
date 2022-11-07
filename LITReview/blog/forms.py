from django import forms


class AbonnementForm(forms.Form):
    utilisateur = forms.CharField(max_length=150)
