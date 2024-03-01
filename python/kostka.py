#!/usr/bin/env python3

import random as ran

class Dice:

    def __init__(self, number_of_sides=6):
        self.number_of_sides = number_of_sides

    def roll(self):
        return ran.randint(1, self.number_of_sides)

if __name__ == "__main__":
    number_of_sides = int(input("Insert a number:"))
    d = Dice(number_of_sides)
    print(d.roll())