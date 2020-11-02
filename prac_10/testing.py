"""
CP1404/CP5632 Practical
Testing demo using assert and doctest
"""

import doctest
import os
import shutil
shutil.move(os.path.join("..", "prac_06", "car.py"), os.getcwd())
from car import Car  # prac_06 is a parallel directory therefore not a valid import option.
shutil.move("car.py", os.path.join("..", "prac_06"))  # __pycache__, therefore not needed.


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    return ' '.join([s] * n)


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length


def run_tests():
    """Run the tests on the functions."""
    print("start")
    # assert test with no message - used to see if the function works properly
    assert repeat_string("Python", 1) == "Python"
    # the test below should *not* fail
    assert repeat_string("hi", 2) == "hi hi"

    # assert test with custom message,
    # used to see if Car's init method sets the odometer correctly
    # this should pass (no output)
    test_car = Car()
    assert test_car.odometer == 0, "Car does not set odometer correctly"

    # Test fuel
    test_car_1 = Car(fuel=10)
    assert test_car_1.fuel == 10, "Custom values not communicated to class"
    test_car_2 = Car()
    assert test_car_2.fuel == 0, "Non-zero default value"

    # Test sentencise function
    assert sentencise('hello') == 'Hello.', sentencise('hello')
    assert sentencise('It is an ex parrot.') == 'It is an ex parrot.', sentencise('It is an ex parrot.')
    assert sentencise('00# thIs Is nOT a sENtENcE') == '00# ThIs Is nOT a sENtENcE.', sentencise('00# thIs Is nOT a sENtENcE')
    try:
        sentencise(1)
    except TypeError:
        print("Success")
    else:
        raise AssertionError("Expected error for type 'int'.")


def sentencise(input_string: str):
    first_letter = ''
    for char in input_string:
        if char.isupper() or char.islower():  # test if letter
            first_letter = char.upper()  # force upper case
            break
    if first_letter:
        position = input_string.upper().find(first_letter)
        input_string = f"{'' if position==0 else input_string[:position]}{first_letter}{input_string[position+1:]}"
    if not input_string.endswith('.'):
        input_string = input_string + '.'
    return input_string


run_tests()
doctest.testmod()
