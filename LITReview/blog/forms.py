from django import forms
from connexion import models


class AbonnementForm(forms.ModelForm):


    class Meta:
        model = models.Abonnement
        fields = ["user_suivi"]
        labels = {"user_suivi": "Nom d'utilisateur"}
        widgets = {"user_suivi": forms.TextInput}
