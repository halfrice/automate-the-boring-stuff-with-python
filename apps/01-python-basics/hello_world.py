#!/usr/bin/env python3

# hello_world.py

print('Hello, world!')
print('What is your name?')  # ask users name
user_name = input()
print('It is good to meet you, ' + user_name)
print('The length of your name is:')
print(len(user_name))
print('What is your age?')  # ask users age
user_age = input()
print('You will be ' + str(int(user_age) + 1) + ' in a year.')
print('Goodbye.')
