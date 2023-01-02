# by: RETBOT
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import UsuarioPers

class FormularioCreacionUsuario(UserCreationForm):
    class Meta(UserCreationForm):
        model = UsuarioPers
        fields = ('username','email',)

# by: RETBOT
class FormularioCambioUsuario(UserChangeForm):
    class Meta:
        model = UsuarioPers
        fields = ('username','email',)
# by: RETBOT
