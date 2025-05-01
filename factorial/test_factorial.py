import unittest

from factorial import factorial_recursivo,factorial_iterativo #importo

class TestFactorialRecursivo(unittest.TestCase):
    def test_simple_recursivo(self):

        self.assertEqual(factorial_recursivo(0), 1)
        self.assertEqual(factorial_recursivo(1), 1)

    def test_with_more_than_1_recursivo(self):
    
        self.assertEqual(factorial_recursivo(2), 2)
        self.assertEqual(factorial_recursivo(5), 120)
        self.assertEqual(factorial_recursivo(20), 2432902008176640000)

    def test_with_nagative_recursivo(self):
        
        self.assertFalse(factorial_recursivo(-1))

class TestFactorialIterativo(unittest.TestCase):
    def test_simple_iterativo(self):

        self.assertEqual(factorial_iterativo(0), 1)
        self.assertEqual(factorial_iterativo(1), 1)

    def test_with_more_than_1_iterativo(self):
    
        self.assertEqual(factorial_iterativo(2), 2)
        self.assertEqual(factorial_iterativo(5), 120)
        self.assertEqual(factorial_iterativo(20), 2432902008176640000)

    def test_with_nagative_iterativo(self):
        
        self.assertFalse(factorial_iterativo(-1))

if __name__ == "__main__":
    unittest.main()