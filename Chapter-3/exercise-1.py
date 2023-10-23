# Exercise 1: Write a function named right_justify that takes a string named s as a parameter and prints the string with
# enough leading spaces so that the least letter of the string is in column 70 of the display

def right_justify(s: str) -> str:
    return (" " * 70) + s

if __name__ == '__main__':
    s = None

    print('Exercise 1')
    while(not isinstance(s, str)):
        s = input('introduce a string: ')

    print(f'\nInput: s = {s}\nOutput:\n{right_justify((s))}')