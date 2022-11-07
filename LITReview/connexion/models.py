from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    abonnement = models.ManyToManyField("self", through="Abonnement",
                                        symmetrical=False)


class Abonnement(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             related_name="qui_suit")
    user_suivi = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                                   on_delete=models.CASCADE,
                                   related_name="suivi_par")

    class Meta:
        unique_together = ("user", "user_suivi")
