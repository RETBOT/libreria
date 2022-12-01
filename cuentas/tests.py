from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse, resolve
from .views import VistaPaginaRegistro
from .forms import FormularioCreacionUsuario

# Create your tests here.
class PruebasPaginaRegistro(TestCase):
  
  def setUp(self):
    url = reverse('singup')
    self.respuesta = self.client.get(url)

  def test_plantilla_registro(self):
    self.assertEqual(self.respuesta.status_code, 200)
    self.assertTemplateNotUsed(self.respuesta, 'registration/signup.html')
    self.assertContains(self.respuesta, 'Registro')
    self.assertNotContains(self.respuesta, '¡Hola! No debería estar en esta página')

  def test_forma_registro(self):
    formulario = self.respuesta.context.get('form')
    self.assertIsInstance(formulario, FormularioCreacionUsuario)
    self.assertContains(self.respuesta, 'csrfmiddlewaretoken')

  def test_vista_registro(self):
    vista = resolve('/cuentas/registro')
    self.assertEqual(vista.func.__name__, VistaPaginaRegistro.as_view().__name__)