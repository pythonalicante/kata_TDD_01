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
    
    array_int_numbers = tuple(int(n) for n in numbers.split(delimiter))
    
    negative_numbers = tuple(str(n) for n in array_int_numbers if n < 0)
    
    if negative_numbers:
        raise ValueError(f"negatives not allowed: {', '.join(negative_numbers)}")
    
    return sum(array_int_numbers)