from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class AbonnementForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["abonnement"]
        labels = {"abonnement": "Nom d'utilisateur"}


# ce form fonctionne mais nous n'avons pas la zone de texte