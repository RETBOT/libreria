#cuentas/models.py
# by: RETBOT
from tokenize import blank_re
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class UsuarioPers(AbstractUser):
    nombre = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    # by: RETBOT
