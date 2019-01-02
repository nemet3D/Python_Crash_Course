# The module random contains functions that generate random numbers in a
# variety of ways . The function randint() returns an integer in the
# range you provide. The following code returns a number between 1 and
# 6: from random import randint
# x = randint(1, 6)
# Make a class Die with one attribute called sides, which has a default
# value of 6. Write a method called roll_die() that prints a random
# number between 1 and the number of sides the die has. Make a 6-sided
# die and rollit 10 times.
# Make a 10-sided die and a 20-sided die. Roll each die 10 times.

from random import randint

class Die():
    """Get a random number."""

    def __init__(self):
        """Initialize for the number of faces of the dice."""
        self.sides = 6

    def roll_die(self, sides):
        """Roll the dice."""
        self.sides = sides
        for i in range(6):
            side = randint(1, int(self.sides))
            print(side)

roll_my_dice = Die()
roll_my_dice.roll_die(49)
