# cuentas/urls.py
from django.urls import path
# by: RETBOT
from .views import VistaPaginaRegistro

urlpatterns = [
    path('registro/', VistaPaginaRegistro.as_view(), name='registro'),
]
# by: RETBOT
