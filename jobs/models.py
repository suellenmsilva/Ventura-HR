from django.db import models
from users.models import CustomUsuario


class Jobs(models.Model):
    TYPE = (
        ('clt', 'CLT'),
        ('temporario', 'Temporario'),
        ('freelance', 'Freelance'),
        ('home_office', 'Home Office'),
    )
    cargo = models.CharField('Cargo', max_length=100, blank=True)
    description = models.TextField('Descrição', max_length=250)
    first_name = models.ForeignKey(CustomUsuario, on_delete=models.CASCADE)
    city = models.CharField('Cidade', max_length=50)
    state = models.CharField('Estado', max_length=50)
    contract_type = models.CharField(max_length=20, choices=TYPE)
    creation_date = models.DateTimeField(auto_now_add=True)
    expiration_date = models.DateField('Data de Expiração')

    def __str__(self):
        return self.cargo, self.first_name, self.contract_type, self.description