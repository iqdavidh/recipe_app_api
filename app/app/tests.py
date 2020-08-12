from django.test import TestCase
from app.calc import add


class CalcTest(TestCase):
    def test_add(self):
        """2 numeros -  basic test"""
        resultado = add(2, 3)
        resultado_esperado = 5
        self.assertEqual(resultado, resultado_esperado)
