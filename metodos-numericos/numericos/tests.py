from django.test import TestCase
import sympy as sp
from numericos.utils import metodo_secante

class MetodoSecanteTest(TestCase):
    def test_secante_convergencia(self):
        x = sp.symbols('x')
        f = sp.sympify('x**2 - 4')

        resultado = metodo_secante(f, x0=1, x1=2)
        
        self.assertIn("raiz", resultado)
        self.assertAlmostEqual(resultado["raiz"], 2, places=5)

    def test_secante_error_division_por_cero(self):
        x = sp.symbols('x')
        f = sp.sympify('x**2 - 4')

        resultado = metodo_secante(f, x0=2, x1=2)  
        self.assertIn("error", resultado)
