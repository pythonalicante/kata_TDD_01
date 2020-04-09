#!/bin/env python

def _check_if_change_delimiter(numbers):
    delimiter = ","
    if "//" in numbers[0:2]:
        delimiter = numbers[2]
        numbers = numbers[4:]
    return delimiter, numbers

def _check_if_typo_in_numbers(delimiter, numbers):
    return f"{delimiter}\n" in numbers or f"\n{delimiter}" in numbers
        

def string_adder(numbers): 
    """The method can take up to two numbers, 
    separated by commas, 
    and will return their sum. 
    
    Parameters
    ----------
    numbers : str
        numbers separeted by comma
    """
    if numbers == "":
        return 0
    
    delimiter, numbers = _check_if_change_delimiter(numbers)

    if _check_if_typo_in_numbers(delimiter, numbers):
        return -1
    
    numbers = numbers.replace('\n', delimiter)
    array_int_numbers = (int(n) for n in numbers.split(delimiter))
    
    return sum(array_int_numbers)
    