from django.contrib import admin
from . import models


class TicketAdmin(admin.ModelAdmin):
    list_display = ("id", "titre", "user", "date")


class CritiqueAdmin(admin.ModelAdmin):
    list_display = ("id", "titre", "ticket", "user", "date")


admin.site.register(models.Ticket, TicketAdmin)
admin.site.register(models.Critique, CritiqueAdmin)
