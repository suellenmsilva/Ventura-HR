from django.contrib.auth import get_user_model
from django.db import models


class Answer(models.Model):
    TYPE_crit = (
        ('ruim', 'Ruim'),
        ('bom', 'Bom'),
        ('muito_bom', 'Muito Bom'),
        ('excelente', 'Excelente'),
    )
    experience = models.CharField('Criterio', max_length=20, choices=TYPE_crit)

    class Meta:
        verbose_name = 'Answer'
        verbose_name_plural = 'Answers'

    def __str__(self):
        return '{}'.format(self.experience)




