# List to Dictionary Function for Fantasy Game Inventory
# inv = {'gold coin': 42, 'rope': 1}
inv = {'gold coin': 42, 'rope': 1, 'warglaive of azzinoth': 1}
dragonLoot = [
    'gold coin',
    'dagger',
    'gold coin',
    'gold coin',
    'ruby',
    'warglaive of azzinoth',
]


def addToInventory(inventory, addedItems):
    for i in range(len(addedItems)):
        item = addedItems[i]
        inventory.setdefault(item, 0)
        inventory[item] += 1

    return inventory


# Fantasy Game Inventory
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}


def displayInventory(inventory):
    print('Inventory:')
    item_total = 0
    for k, v in inventory.items():
        print(f'{v} {k}')
        item_total += v
    print('total number of items: ' + str(item_total))


# displayinventory(stuff)
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
