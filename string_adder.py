#!/bin/env python


def string_adder(numbers):
    """The method can take up to two numbers, 
    separated by commas, 
    and will return their sum. 
    
    Parameters
    ----------
    numbers : str
        numbers separeted by comma
    """
    if numbers != "":
        array_str_numbers = numbers.split(",")
        array_int_numbrs = [int(n) for n in array_str_numbers]
        return sum(array_int_numbrs)
    else:
        return 0