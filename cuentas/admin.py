# by: RETBOT
# cuentas/admin.py 
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from .forms import FormularioCreacionUsuario, FormularioCambioUsuario

UsuarioPers = get_user_model()
# by: RETBOT
class UsuarioAdmin(UserAdmin):
  add_form = FormularioCreacionUsuario
  form = FormularioCambioUsuario
  model = UsuarioPers
  list_display = [
  'email',
  'username',
  'is_superuser',
  ]

# Register your models here.
admin.site.register(UsuarioPers, UsuarioAdmin)
# by: RETBOT
