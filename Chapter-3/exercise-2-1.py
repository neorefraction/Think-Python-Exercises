# Author: @neorefraction
# Date: 23-10-23

# Exercise 2.1: A function objet is a value you can assign to a variable or pass as an argument. Fot example, do_twice
# is a function that takes a function object as an argument nad calls it twice.
# Type this example into a script and test it.

from typing import Callable  # Callable is a type used to reference to functions


# 'f: Callable' specify the data type expected for this parameter and
# '-> None' specify the data type expected for the returned value
def do_twice(f: Callable) -> None:
    """
    Call twice a function passed as argument
    :param f: a function to be called
    :return: None
    """
    f()
    f()


def print_spam() -> None:
    """
    Prints 'spam'
    :return: None
    """
    print('spam')


if __name__ == '__main__':

    print('Exercise 2.1')
    do_twice(print_spam)
