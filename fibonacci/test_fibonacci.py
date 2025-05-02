import unittest

from fibonacci import fibonacci_recursiva, fibonacci_iterativa
class TestFibonaccil(unittest.TestCase):
    #casos de prueba de con fibonacci recursiva
    def test_simple_recursiva(self): #casos de prueba para numeros simples y 0

        self.assertEqual(fibonacci_recursiva(0),0)
        self.assertEqual(fibonacci_recursiva(1),1)
        self.assertEqual(fibonacci_recursiva(2),1)
        self.assertEqual(fibonacci_recursiva(3),2)
        self.assertEqual(fibonacci_recursiva(4),3)
        self.assertEqual(fibonacci_recursiva(5),5)
    def test_complex_recursiva(self): #casos de pueba para numeros complejos con resultados complejos
        self.assertEqual(fibonacci_recursiva(6),8)
        self.assertEqual(fibonacci_recursiva(7),13)
        self.assertEqual(fibonacci_recursiva(12),144)
        self.assertEqual(fibonacci_recursiva(15),610)
    def test_with_nagative_recursiva(self): #casos de prueba para nuemero negativo
        
        with self.assertRaises(ValueError):
            fibonacci_recursiva(-1)

    #casos de prueba de con fibonacci iterativa
    def test_simple_iterativa(self): #casos de prueba para numeros simples y 0

        self.assertEqual(fibonacci_iterativa(0),0)
        self.assertEqual(fibonacci_iterativa(1),1)
        self.assertEqual(fibonacci_iterativa(2),1)
        self.assertEqual(fibonacci_iterativa(3),2)
        self.assertEqual(fibonacci_iterativa(4),3)
        self.assertEqual(fibonacci_iterativa(5),5)
    def test_complex_iterativa(self): #casos de pueba para numeros complejos con resultados complejos
        self.assertEqual(fibonacci_iterativa(6),8)
        self.assertEqual(fibonacci_iterativa(7),13)
        self.assertEqual(fibonacci_iterativa(12),144)
        self.assertEqual(fibonacci_iterativa(15),610)
    def test_with_nagative_iterativa(self): #casos de prueba para nuemero negativo
        
        with self.assertRaises(ValueError):
            fibonacci_iterativa(-1)

if __name__ == "__main__":
    unittest.main()