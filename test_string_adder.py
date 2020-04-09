import unittest

from string_adder import string_adder

class TestStringAdder(unittest.TestCase):

    def test_sum_two_numbers(self): 
        # Inicializacion
        param = "1,2"
        expected = 3
        # Accion
        result = string_adder(param)
        # Comprobacion
        self.assertEqual(expected, result)

    def test_empty_params(self): 
        # Inicializacion
        param = ""
        expected = 0
        # Accion
        result = string_adder(param)
        # Comprobacion
        self.assertEqual(expected, result)

    def test_sum_one_number(self): 
        # Inicializacion
        param = "1"
        expected = 1
        # Accion
        result = string_adder(param)
        # Comprobacion
        self.assertEqual(expected, result)        

    def test_a_lot_of_numbers(self):
        # Inicializacion
        param = "1,2,3,4,5,6,7,8"
        expected = 36
        # Accion
        result = string_adder(param)
        # Comprobacion
        self.assertEqual(expected, result) 

if __name__ == '__main__':
    unittest.main()
