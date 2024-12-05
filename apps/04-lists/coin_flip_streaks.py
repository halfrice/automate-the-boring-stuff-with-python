#!/usr/bin/evn python3

# coin_clip_streaks.py

import random

number_of_streaks = 0
for experiment_number in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    coin_flips = []
    for i in range(100):
        coin_flips.append(random.randint(0, 1))

    # Code that checks if there is a streak of 6 heads or tails in a row.
    streak = 1
    for i in range(1, len(coin_flips)):
        if coin_flips[i] == coin_flips[i - 1]:
            streak += 1
        else:
            streak = 1

        if streak == 6:
            number_of_streaks += 1
            break


print('Chance of streak: %s%%' % (number_of_streaks / 100))
