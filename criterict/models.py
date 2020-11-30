from django.db import models


class Criterict(models.Model):
    TYPE = (
        ('ruim', 'Ruim'),
        ('bom', 'Bom'),
        ('muito_bom', 'Muito Bom'),
        ('excelente', 'Excelente'),
    )

    experience = models.CharField(max_length=20, choices=TYPE)
    criterict = models.CharField('Criterio', max_length=100, blank=True)
