from django.contrib.auth import get_user_model
from django.db import models

from criterict.models import Criterict


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
    criterict = models.ForeignKey(Criterict, on_delete=models.CASCADE)

    def __str__(self):
        return self.cargo, self.user, self.contract_type, \
               self.description