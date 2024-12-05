#!/usr/bin/env python3

# collatz_sequence.py


def collatz(number):
    if number % 2 == 0:
        n = number // 2
    else:
        n = (number * 3) + 1
    print(n)
    return n


number_input = int(input('Enter number:\n'))
while number_input > 1:
    number_input = collatz(number_input)
