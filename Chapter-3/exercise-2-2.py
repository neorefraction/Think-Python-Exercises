# Author: @neorefraction
# Date: 23-10-23

# Exercise 2.1: A function objet is a value you can assign to a variable or pass as an argument. Fot example, do_twice
# is a function that takes a function object as an argument nad calls it twice.
# Type this example into a script and test it.

from typing import Callable  # Callable is a type used to reference to functions


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


if __name__ == '__main__':

    print('Exercise 2.2')
    do_twice(print, 'Hello world!')  # Watch out!! built-in print function is passed not print_spam
