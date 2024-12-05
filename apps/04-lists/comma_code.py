#!/usr/bin/evn python3

# comma_code.py


def comma(string_list):
    string = ''
    len_of_string_list = len(string_list)
    if len_of_string_list == 1:
        return string_list[0]
    elif len_of_string_list == 2:
        return ' and '.join(string_list)
    elif len_of_string_list > 2:
        for i in range(len_of_string_list):
            if i == len_of_string_list - 1:
                string += f'and {string_list[i]}'
            else:
                string += f'{string_list[i]}, '
    return string


user_list = []
item_count = 0
print('Enter items to your list. Enter nothing to finish.')
while True:
    user_input = input(f'{item_count+1}: ')
    if user_input.isalnum():
        user_list.append(user_input)
        item_count += 1
    elif user_input == '':
        if len(user_list) == 0:
            print('You have entered an empty list. You lose.')
        else:
            print(comma(user_list))
        break
    else:
        print('Invalid input. Try Again.')

# Test cases
# spam = ['apples', 'bananas', 'tofu', 'cats']
# print(comma(spam))
# print(comma(spam[:2]))
# print(comma(spam[:1]))
# print(comma([]))
