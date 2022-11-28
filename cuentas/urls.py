# cuentas/urls.py
from django.urls import path

from .views import VistaPaginaRegistro

urlpatterns = [
    path('registro/', VistaPaginaRegistro.as_view(), name='registro'),
]
