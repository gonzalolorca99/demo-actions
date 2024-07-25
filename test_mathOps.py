# test_mathOps.py

import unittest
from mathOps import sumar,restar,multiplicar,dividir

class TestMathOps(unittest.TestCase):

    def test_sumar(self):
        self.assertEqual(sumar(3, 2), 5)
        self.assertEqual(sumar(-1, 1), 0)
        self.assertEqual(sumar(-1, -1), -2)
        self.assertEqual(sumar(0, 0), 0)
        self.assertEqual(sumar(999999, 1), 1000000)

    def test_restar(self):
        self.assertEqual(restar(3, 2), 1)
        self.assertEqual(restar(-1, 1), -2)
        self.assertEqual(restar(-1, -1), 0)
        self.assertEqual(restar(0, 0), 0)
        self.assertEqual(restar(999999, 1), 999998)

    def test_multiplicar(self):
        self.assertEqual(multiplicar(3, 2), 6)
        self.assertEqual(multiplicar(-1, 1), -1)
        self.assertEqual(multiplicar(-1, -1), 1)
        self.assertEqual(multiplicar(0, 0), 0)
        self.assertEqual(multiplicar(999999, 1), 999999)

    def test_dividir(self):
        self.assertEqual(dividir(6, 2), 3)
        self.assertEqual(dividir(-6, 2), -3)
        self.assertEqual(dividir(-6, -2), 3)
        self.assertEqual(dividir(0, 1), 0)
        self.assertEqual(dividir(1, 0), "Error: No se puede dividir por cero")
        self.assertEqual(dividir(999999, 1), 999999)

if __name__ == '__main__':
    unittest.main()
