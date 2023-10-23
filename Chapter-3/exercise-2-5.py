# Author: @neorefraction
# Date: 23-10-23

# Exercise 2.1: A function objet is a value you can assign to a variable or pass as an argument. Fot example, do_twice
# is a function that takes a function object as an argument nad calls it twice.
# Type this example into a script and test it.

from typing import Callable, Any  # Callable is a type used to reference to functions and Any to any type


# 'f: Callable' and 'value: str' specify the data type expected for these parameters and
# '-> None' specify the data type expected for the returned value
def do_twice(f: Callable, value: str) -> None:  # '-> None' is similar to say 'return void'
    """
    Call twice a function passed as argument
    :param f: A function to be called
    :param value: The value to be passed to f
    :return: None
    """
    f(value)
    f(value)


def print_spam() -> None:
    """
    Prints 'spam'
    :return: None
    """
    print('spam')


def print_twice(bruce: Any) -> None:
    """
    Prints the value of bruce two times
    :param bruce: The string to be printed
    :return: None
    """
    print(bruce)
    print(bruce)


def do_four(f: Callable, value: str) -> None:
    """
    Calls four times to the function 'f' using 'do_twice' function.
    :param f: Function to be called
    :param value: A value to pass as argument to the function 'f'
    :return: None
    """
    do_twice(print_twice, value)
    do_twice(print_twice, value)


if __name__ == '__main__':

    print('Exercise 2.5')
    do_four(print_twice, 'spam')
