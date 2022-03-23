from django.db import models
from datetime import datetime, timedelta
from django.utils import timezone

class urls(models.Model):
    url_normal = models.URLField(verbose_name='URL', unique=True)
    url_encurtada = models.CharField(verbose_name='URL Menor', max_length=20, blank=True, null=True, unique=True)
    data_criacao = models.DateField(auto_now_add=True, verbose_name='Data de Criação')
    data_expiracao = models.DateField(verbose_name='Data de Expiração', null=True, blank=True)

    def get_data_de_criacao(self):
        return self.data_criacao.strftime('%d/%m/%Y - %H:%M:%S')

    def get_data_de_expiracao(self):
        return self.data_expiracao.strftime('%d/%m/%Y')

    def __str__(self):
        return f'{self.url_normal}'

