from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from PIL import Image


class Ticket(models.Model):
    titre = models.CharField(max_length=128)
    description = models.TextField(max_length=2048, blank=True)
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)


class Critique(models.Model):
    ticket = models.ForeignKey(to=Ticket, on_delete=models.CASCADE)
    note = models.PositiveSmallIntegerField(validators=[MinValueValidator(0),
                                                        MaxValueValidator(5)])
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    titre = models.CharField(max_length=128)
    commentaire = models.TextField(max_length=8192, blank=True)
    date = models.DateTimeField(auto_now_add=True)
