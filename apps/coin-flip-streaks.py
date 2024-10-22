import random

numberOfStreaks = 0
for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    coinFlips = []
    for i in range(100):
        coinFlips.append(random.randint(0, 1))

    # Code that checks if there is a streak of 6 heads or tails in a row.
    streak = 1
    for i in range(1, len(coinFlips)):
        if coinFlips[i] == coinFlips[i - 1]:
            streak += 1
        else:
            streak = 1

        if streak == 6:
            numberOfStreaks += 1
            break


print('Chance of streak: %s%%' % (numberOfStreaks / 100))
