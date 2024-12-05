#!/usr/bin/evn python3

# fantasy_game_inventory_list_to_dictionary_function.py


def add_to_inventory(added_items, inventory):
    for i in range(len(added_items)):
        item = added_items[i]
        inventory.setdefault(item, 0)
        inventory[item] += 1
    return inventory


def display_inventory(inventory):
    print('Inventory:')
    item_total = 0
    for k, v in inventory.items():
        print(f'{v} {k}')
        item_total += v
    print('total number of items: ' + str(item_total))


stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
inv = {'gold coin': 42, 'rope': 1, 'warglaive of azzinoth': 1}
dragon_loot = [
    'gold coin',
    'dagger',
    'gold coin',
    'gold coin',
    'ruby',
    'warglaive of azzinoth',
]

inv = add_to_inventory(dragon_loot, inv)
display_inventory(inv)
