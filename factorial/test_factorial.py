import unittest

from factorial import factorial_recursivo,factorial_iterativo #importo las funciones del archivo de impletación

class TestFactorialRecursivo(unittest.TestCase): # casos de prueba para la funcion recursiva
    def test_simple_recursivo(self): #casos de prueba para cero y uno

        self.assertEqual(factorial_recursivo(0), 1)
        self.assertEqual(factorial_recursivo(1), 1)

    def test_with_more_than_1_recursivo(self): #casos de prueba para numero mayores a 1
    
        self.assertEqual(factorial_recursivo(2), 2)
        self.assertEqual(factorial_recursivo(5), 120)
        self.assertEqual(factorial_recursivo(20), 2432902008176640000)

    def test_with_nagative_recursivo(self): #casos de prueba para nuemero negativo
        
        with self.assertRaises(ValueError):
            factorial_iterativo(-1)

class TestFactorialIterativo(unittest.TestCase): # casos de prueba para la funcion iterativa
    def test_simple_iterativo(self): #casos de prueba para cero y uno

        self.assertEqual(factorial_iterativo(0), 1)
        self.assertEqual(factorial_iterativo(1), 1)

    def test_with_more_than_1_iterativo(self): #casos de prueba para numero mayores a 1
    
        self.assertEqual(factorial_iterativo(2), 2)
        self.assertEqual(factorial_iterativo(5), 120)
        self.assertEqual(factorial_iterativo(20), 2432902008176640000)

    def test_with_nagative_iterativo(self): #casos de prueba para nuemero negativo
        
        with self.assertRaises(ValueError):
            factorial_iterativo(-1)

if __name__ == "__main__":
    unittest.main()