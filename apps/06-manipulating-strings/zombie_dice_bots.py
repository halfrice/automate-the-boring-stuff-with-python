#!/usr/bin/env python3

# zombie_dice_bots.py

import random
import zombiedice


class Zombie:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, game_state):
        # game_state is a dict with info about the current state of the game.

        dice_roll_results = zombiedice.roll()
        # Example of a roll() return value:
        # {
        #    'brains': 1,
        #    'footsteps': 1,
        #    'shotgun': 1,
        #    'rolls': [
        #        ('yellow', 'brains'),
        #        ('red', 'footsteps'),
        #        ('green', 'shotgun')
        #    ],
        # }

        brains = 0
        while dice_roll_results is not None:
            brains += dice_roll_results['brains']
            if brains < 2:
                dice_roll_results = zombiedice.roll()  # roll again
            else:
                break


class RandomZombie(Zombie):
    """Randomly decides to continue or stop after the first roll"""

    def __init__(self, name):
        super().__init__(name)

    def turn(self, game_state):
        dice_roll_results = zombiedice.roll()
        while dice_roll_results:
            coin_flip = random.randint(0, 1)
            if coin_flip:
                dice_roll_results = zombiedice.roll()
            else:
                break


class BrainsZombie(Zombie):
    """Stops playing after user-specified amount of brains aquired"""

    def __init__(self, name, min_brains=3):
        super().__init__(name)
        self.min_brains = min_brains

    def turn(self, game_state):
        brains = 0
        while brains < self.min_brains:
            dice_roll_results = zombiedice.roll()
            if not dice_roll_results:
                break
            brains += dice_roll_results['brains']


class ShotgunsZombie(Zombie):
    """Stops playing after user-specified amount of shotguns aquired"""

    def __init__(self, name, min_shotguns=2):
        super().__init__(name)
        self.min_shotguns = min_shotguns

    def turn(self, game_state):
        shotguns = 0
        while shotguns < self.min_shotguns:
            dice_roll_results = zombiedice.roll()
            if not dice_roll_results:
                break
            shotguns += dice_roll_results['shotgun']


class NRollsZombie(Zombie):
    """Rolls 1-4 times before but stops early if two shotguns aquired"""

    def __init__(self, name):
        super().__init__(name)
        self.max_rolls = random.randint(1, 4)
        self.min_shotguns = 2

    def turn(self, game_state):
        rolls = 0
        shotguns = 0
        while rolls < self.max_rolls:
            dice_roll_results = zombiedice.roll()
            if not dice_roll_results:
                break
            rolls += 1
            shotguns += dice_roll_results['shotgun']
            if shotguns >= self.min_shotguns:
                break


class OddsZombie(Zombie):
    """Stops rolling after it rolls more shotguns than brains"""

    def __init__(self, name):
        super().__init__(name)

    def turn(self, game_state):
        brains = 0
        shotguns = 0
        while shotguns <= brains:
            dice_roll_results = zombiedice.roll()
            if not dice_roll_results:
                break
            brains += dice_roll_results['brains']
            shotguns += dice_roll_results['shotgun']


zombies = (
    RandomZombie(name='Random Phantom'),
    BrainsZombie(name='2 Brainz', min_brains=2),
    ShotgunsZombie(name='Dos Gunna', min_shotguns=2),
    NRollsZombie(name='Predetermined Fate'),
    OddsZombie(name='Cautious Pansy'),
    BrainsZombie(name='Degenerate Gambler', min_brains=13),
)

# Uncomment to run in CLI or Web GUI mode:
# zombiedice.runTournament(zombies=zombies, numGames=1000)
zombiedice.runWebGui(zombies=zombies, numGames=1000)
