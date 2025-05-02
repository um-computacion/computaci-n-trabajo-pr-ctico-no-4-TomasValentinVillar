import unittest

from flatten import aplanar_lista #irmportar funcion aplanar lista de flatten.py

class TestAplanarLista(unittest.TestCase):

    def test_caso_lista_simple(self):  #casos de prueba para listas simples
        self.assertEqual(aplanar_lista([1, 2, 3, 4]),[1, 2, 3, 4])
    
    def test_caso_listas_anidadas(self): #casos de prueba para listas anidadas 
        self.assertEqual(aplanar_lista([1, [2, 3], [4, [5, 6]]]),[1, 2, 3, 4, 5, 6])

    def test_caso_lista_diferentes_estructuras(self): #casos de prueba para listas de diferentes estructuras
        self.assertEqual(aplanar_lista([1, (2, 3), {'a': 4, 'b': 5}, [6, [7, 8]]]), [1, 2, 3, 'a', 4, 'b', 5, 6, 7, 8])

if __name__ == "__main__":
    unittest.main()