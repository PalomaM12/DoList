from django.db import models
from django.conf import settings
from apps.core.models import Categoria

class Tarefa(models.Model):
    
    titulo = models.CharField(max_length=200)
    descricao = models.TextField(blank=True, null=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    concluida = models.BooleanField(default=False)
    prazo = models.DateField(null=True, blank=True) 
    
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='tarefas_criadas')
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True, related_name='tarefas_classificadas')

    def __str__(self):
        return self.titulo

