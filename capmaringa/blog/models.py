from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    titulo = models.CharField(max_length=75)
    descricao = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    data_publicacao = models.DateTimeField()
    imagem = models.ImageField(upload_to='imagens/', blank=True, null=True)

    def __str__(self):
        return self.titulo