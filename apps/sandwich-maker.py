import pyinputplus as pyip

breadTypes = ['wheat', 'white', 'sourdough']
proteinTypes = {'chicken': 1999, 'turkey': 1899, 'ham': 1949, 'tofu': 1699}
cheeseTypes = ['cheddar', 'swiss', 'mozzarella']
condimentTypes = ['mayo', 'mustard', 'lettuce', 'tomato']


while True:
    cost = 0

    print('Welcome to Sandwich Maker. I love you.')
    bread = pyip.inputMenu(breadTypes, prompt='What type of bread you want?\n')

    protein = pyip.inputMenu(list(proteinTypes.keys()), prompt='What kinda meat?\n')

    isCheeseAdded = pyip.inputYesNo(
        "You want cheese on that? It's five bucks extra. (y/n)\n"
    )
    if isCheeseAdded:
        cheese = pyip.inputMenu(cheeseTypes, 'What type of cheese?\n')
        cost += 499

    condiments = []
    for i in range(len(condimentTypes)):
        condiment = condimentTypes[i]
        if pyip.inputYesNo(f'Do you want {condiment}? (y/n)\n'):
            condiments.append(condiment)

    count = pyip.inputInt('How many of these sandwiches do you want?\n', min=1)
    for i in range(count):
        cost += proteinTypes[protein]

    cost = cost / 100
    tax = cost * 0.097
    costOfLivingSurcharge = (cost + tax) * 0.25  # Because you live in Palo Alto
    total = cost + tax + costOfLivingSurcharge
    print(f"That'll be ${total:.2f}. Thank you, come again.")

    # Extra credit: Give the user a receipt for their order
    # Something like below. Try using rjust / ljust to make it look realistic 👍
    # receipt = pyip.inputYesNo('You want a receipt? (y/n)\n')
    # if receipt:
    #     print(f'{protein.title()} Sandwich - ${proteinTypes[protein]/100:.2f}')
    #     ...
    #     ...

    break
