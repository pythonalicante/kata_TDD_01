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
        if ",\n" in numbers or "\n," in numbers:
            return -1
        numbers = numbers.replace('\n', ",")
        array_str_numbers = numbers.split(",")
        array_int_numbrs = [int(n) for n in array_str_numbers]
        return sum(array_int_numbrs)
    else:
        return 0