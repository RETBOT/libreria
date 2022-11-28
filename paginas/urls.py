# paginas/urls.py
from django.urls import path

from .views import VistaPaginaInicio

urlpatterns = [
    path('', VistaPaginaInicio.as_views(), name='inicio'),
]
