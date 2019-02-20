from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Aviso(models.Model):
    titulo = models.CharField(max_length=75)
    descricao = models.TextField()
    data = models.DateField()
    horario = models.TimeField()
    lugar = models.CharField(max_length=50)         # Ex: Casa do joao
    endereco = models.CharField(max_length=75)      # Ex: rua bananal n 001
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

    def ja_aconteceu(self):
        if timezone.localdate() > self.data:
            return True
        else:
            return False