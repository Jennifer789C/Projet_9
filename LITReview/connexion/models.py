from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Abonnement(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             related_name="suivi_par")
    user_suivi = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                                   on_delete=models.CASCADE,
                                   related_name="user_suivi")

    class Meta:
        unique_together = ("user", "user_suivi")