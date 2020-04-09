import unittest

from string_adder import string_adder

class TestStringAdder(unittest.TestCase):

    def test_sum_two_numbers_gt_10(self): 
        # Inicializacion
        param = "11,22"
        expected = 33
        # Accion
        result = string_adder(param)
        # Comprobacion
        self.assertEqual(expected, result)

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

    def test_accept_backslash_n(self):
        # Inicializacion
        param = "1\n2,3"
        expected = 6
        # Accion
        result = string_adder(param)
        # Comprobacion
        self.assertEqual(expected, result) 

    def test_not_accept_comma_backslash_n(self):
        # Inicializacion
        param = "1,\n"
        expected = -1
        # Accion
        result = string_adder(param)
        # Comprobacion
        self.assertEqual(expected, result)

    def test_accept_backslash_n_and_commas(self):
        # Inicializacion
        param = "1\n2,3\n4,5"
        expected = 15
        # Accion
        result = string_adder(param)
        # Comprobacion
        self.assertEqual(expected, result) 

    def test_can_change_delimiter(self):
        # Inicializacion
        param = "//;\n1;2;3"
        expected = 6
        # Accion
        result = string_adder(param)
        # Comprobacion
        self.assertEqual(expected, result) 

    def test_can_change_delimiter_to_amp(self):
        # Inicializacion
        param = "//&\n1&2&3"
        expected = 6
        # Accion
        result = string_adder(param)
        # Comprobacion
        self.assertEqual(expected, result) 

    def test_can_change_delimiter_and_typo(self):
        # Inicializacion
        param = "//;\n1;\n2;3"
        expected = -1
        # Accion
        result = string_adder(param)
        # Comprobacion
        self.assertEqual(expected, result) 

    def test_no_accept_one_negative(self):
        # Inicializacion
        param = "-1,2,3"
        expected = "negatives not allowed: -1"
        # Accion
        with self.assertRaises(ValueError) as context:
            result = string_adder(param)
        print(context.exception)
        # Comprobacion
        self.assertEqual(expected, f"{expected}") 

    def test_no_accept_negatives(self):
                # Inicializacion
        param = "-1,2,-3"
        expected = "negatives not allowed: -1, -3"
        # Accion
        with self.assertRaises(ValueError) as context:
            result = string_adder(param)
        print(context.exception)
        # Comprobacion
        self.assertEqual(expected, f"{expected}") 

    def test_ignore_numbers_greater_than_1000(self):
        # Inicializacion
        param = "1,2,3,1001"
        expected = 6
        # Accion
        result = string_adder(param)
        # Comprobacion
        self.assertEqual(expected, result) 

if __name__ == '__main__':
    unittest.main()
