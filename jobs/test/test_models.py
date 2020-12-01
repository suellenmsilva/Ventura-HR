import unittest
from django.test import TestCase
from model_mommy import mommy


class JobsTestCase(unittest.TestCase):
    def setUp(self):
        self.cargo = mommy.make('Jobs')

    def test_str(self):
        self.assertEquals(str(self.cargo), self.cargo.cargo)


class CriterioTestCase(TestCase):
    def setUp(self):
        self.criterict = mommy.make('Criterio')

    def test_str(self):
        self.assertEquals(str(self.criterict), self.criterict.criterict)