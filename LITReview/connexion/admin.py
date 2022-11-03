from django.contrib import admin
from . import models


class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "id", "is_superuser")


class AbonnementAdmin(admin.ModelAdmin):
    list_display = ("user", "user_suivi")


admin.site.register(models.User, UserAdmin)
admin.site.register(models.Abonnement, AbonnementAdmin)
