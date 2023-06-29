from .models import Usuarios
from django.db import transaction
from django.contrib.auth.forms import UserCreationForm



class RegistrarUsuariosForm(UserCreationForm):

    class Meta:
        model = Usuarios
        fields = ['nombre','apellido','fecha_nacimiento','username','password1','password2','email','imagen']

    @transaction.atomic
    def save(self):
        user              = super().save(commit=False)
        user.is_superuser = False
        user.is_staff     = False
        user.save()
        return user