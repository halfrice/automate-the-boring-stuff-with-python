#!/usr/bin/env python3

# input_validation.py


def collatz(number):
    if number % 2 == 0:
        n = number // 2
    else:
        n = (number * 3) + 1
    print(n)
    return n


while True:
    number_input = input('Enter number:\n')
    try:
        number_input = int(number_input)
        break
    except ValueError:
        print('Invalid input. Enter an integer.')

while number_input > 1:
    number_input = collatz(number_input)
