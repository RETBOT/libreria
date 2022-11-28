from audioop import reverse
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import FormularioCreacionUsuario

# Create your views here.
class VistaPaginaRegistro(CreateView):
    form_class = FormularioCreacionUsuario
    success_url = reverse_lazy('login')
    template_name = 'registration/registro'