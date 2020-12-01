from django.test import TestCase
from model_mommy import mommy

from jobs.forms import JobModelForm


class JobModelFormTestCase(TestCase):
    def setUp(self):
        self.cargo = 'Desenvolvedor Web'
        self.description = 'Texto qualquer'
        self.city = 'Rio de Janeiro'
        self.state = 'Rio de Janeiro'
        self.contract_type = 'CLT'
        self.expiration_date = '30/11/2020'
        self.criterict = 'Teste'

        self.dados = {
            'cargo': self.cargo,
            'description': self.description,
            'city': self.city,
            'state': self.state,
            'contract_type': self.contract_type,
            'expiration_date': self.criterict
        }
        self.form = JobModelForm(data=self.dados) #JobModelForm(request.POST)

    def test_send_mail(self):
        form1 = ContatoForm(data=self.dados)
        form1.is_valid()
        res1 = form1.send_mail()

        form2 = self.form
        form2.is_valid()
        res2 = form2.send_mail()

        self.assertEquals(res1, res2)