#!/usr/bin/env python3

# sandwich_maker.py

import pyinputplus as pyip

bread_types = ['wheat', 'white', 'sourdough']
protein_types = {'chicken': 1999, 'turkey': 1899, 'ham': 1949, 'tofu': 1699}
cheese_types = ['cheddar', 'swiss', 'mozzarella']
condiment_types = ['mayo', 'mustard', 'lettuce', 'tomato']

while True:
    cost = 0

    print('Welcome to Sandwich Maker. I love you.')
    bread = pyip.inputMenu(bread_types, prompt='What type of bread you want?\n')

    protein = pyip.inputMenu(list(protein_types.keys()), prompt='What kinda meat?\n')

    is_cheese_added = pyip.inputYesNo(
        "You want cheese on that? It's five bucks extra. (y/n)\n"
    )
    if is_cheese_added:
        cheese = pyip.inputMenu(cheese_types, 'What type of cheese?\n')
        cost += 499

    condiments = []
    for i in range(len(condiment_types)):
        condiment = condiment_types[i]
        if pyip.inputYesNo(f'Do you want {condiment}? (y/n)\n'):
            condiments.append(condiment)

    count = pyip.inputInt('How many of these sandwiches do you want?\n', min=1)
    for i in range(count):
        cost += protein_types[protein]

    cost = cost / 100
    tax = cost * 0.097
    cost_of_living_surcharge = (cost + tax) * 0.25  # Because you live in Palo Alto
    total = cost + tax + cost_of_living_surcharge
    print(f"That'll be ${total:.2f}. Thank you, come again.")

    # Extra credit: Give the user a receipt for their order
    # Something like below. Try using rjust / ljust to make it look realistic 👍
    # receipt = pyip.inputYesNo('You want a receipt? (y/n)\n')
    # if receipt:
    #     print(f'{protein.title()} Sandwich - ${protein_types[protein]/100:.2f}')
    #     ...
    #     ...

    break
