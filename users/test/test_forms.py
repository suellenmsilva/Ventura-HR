from django.test import TestCase
from model_mommy import mommy

from users.forms import CustomUsuarioCreateForm


class CustomUsuarioCreateFormTestCase(TestCase):
    def setUp(self):
        self.username = 'teste@teste.com'
        self.first_name = 'Texto qualquer'
        self.last_name = 'Texto qualquer'
        self.fone = '21999999999'
        self.groups = 'Empresa'

        self.dados = {
            'username': self.username,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'fone': self.fone,
            'groups': self.groups,

        }
        self.form = CustomUsuarioCreateForm(data=self.dados) #request.POST)

    def test_save(self):
        form1 = CustomUsuarioCreateForm(data=self.dados)
        form1.is_valid()
        res1 = form1.save()

        form2 = self.form
        form2.is_valid()
        res2 = form2.save()

        self.assertEquals(res1, res2)