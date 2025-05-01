import unittest

from factorial import factorial_recursivo

class TestFactorial(unittest.TestCase):
    def test_simple(self):

        self.assertEqual(factorial_recursivo(0), 1)
        self.assertEqual(factorial_recursivo(1), 1)

    def test_with_more_than_1(self):
    
        self.assertEqual(factorial_recursivo(2), 2)
        self.assertEqual(factorial_recursivo(5), 120)
        self.assertEqual(factorial_recursivo(20), 2432902008176640000)

    def test_with_nagative(self):
        
        self.assertFalse(factorial_recursivo(-1))


if __name__ == "__main__":
    unittest.main()