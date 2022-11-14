"""LITReview URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
import connexion.views
import blog.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", LoginView.as_view(template_name="connexion.html",
                               redirect_authenticated_user=True),
         name="connexion"),
    path("deconnexion/", LogoutView.as_view(), name="deconnexion"),
    path("inscription/", connexion.views.inscription_page, name="inscription"),
    path("abonnements/", connexion.views.suivre_user, name="abonnements"),
    path("abonnement/<int:abonnement_id>/delete/", connexion.views.desabonner,
         name="désabonnement"),
    path("flux/", blog.views.flux, name="flux"),
    path("posts/", blog.views.posts, name="posts"),
    path("ticket/creer/", blog.views.creer_ticket, name="creer_ticket"),
    path("ticket/<int:ticket_id>/modifier/", blog.views.modifier_ticket,
         name="modifier_ticket"),
    path("critique/creer/", blog.views.creer_critique_et_ticket,
         name="creer_critique"),
    path("critique/<int:critique_id>/modifier/",
         blog.views.modifier_critique_et_ticket, name="modifier_critique"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
