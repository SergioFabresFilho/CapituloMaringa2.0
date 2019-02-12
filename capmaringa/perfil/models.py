from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Se a conta esta autorizada para fazer login
    conta_autorizada = models.BooleanField(default=False)

    # Se a conta pode adicionar posts e avisos
    pode_postar = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username