from django import forms


class AbonnementForm(forms.Form):
    username = forms.CharField(max_length=150)
