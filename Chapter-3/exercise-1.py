# Author: @neorefraction
# Date: 23-10-23

# Exercise 1: Write a function named right_justify that takes a string named s as a parameter and prints the string
# with enough leading spaces so that the least letter of the string is in column 70 of the display

# 's: str' specify the data type expected for this parameter and
# '-> str' specify the data type expected for the returned value
def right_justify(s: str) -> str:
    """
    Justify a text 70 right spaces
    :param s: The string to be justified
    :return: The string justified
    """
    return (" " * 70) + s


# This condition evaluate what happens if the file is executed as main
if __name__ == '__main__':
    input_string = None

    print(type(right_justify))

    print('Exercise 1')
    while not isinstance(input_string, str):
        input_string = input('introduce a string: ')

    print(f'\nInput: s = {input_string}\nOutput:\n{right_justify(input_string)}')
