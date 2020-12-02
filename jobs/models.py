from django.contrib.auth import get_user_model, get_user, login
from django.db import models


class Criterio(models.Model):
    criterict = models.CharField('Criterio', max_length=100, blank=True)

    def __str__(self):
        return '{}  '.format(self.criterict)


class Jobs(models.Model):
    TYPE = (
        ('clt', 'CLT'),
        ('temporario', 'Temporario'),
        ('freelance', 'Freelance'),
        ('home_office', 'Home Office'),
    )

    cargo = models.CharField('Cargo', max_length=100, blank=True)
    description = models.TextField('Descrição', max_length=250)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    city = models.CharField('Cidade', max_length=50)
    state = models.CharField('Estado', max_length=50)
    contract_type = models.CharField(max_length=20, choices=TYPE)
    creation_date = models.DateTimeField(auto_now_add=True)
    expiration_date = models.DateField('Data de Expiração')
    criterict = models.ManyToManyField(Criterio)

    def __str__(self):
        return '{} '.format(self.cargo)


class Aplication(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    jobs = models.ForeignKey(Jobs, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Aplication'
        verbose_name_plural = 'Aplications'
        unique_together = ['user', 'jobs']

    def __str__(self):
        return '{} {}'.format(self.user, self.jobs)
