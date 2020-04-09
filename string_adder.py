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
        commas_count = numbers.count(",")
        if commas_count == 0:
            return int(numbers)
        else:
            number_a, number_b = numbers.split(",")
        return int(number_a) + int(number_b)
    else:
        return 0