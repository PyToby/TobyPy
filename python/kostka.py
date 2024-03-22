#!/usr/bin/env python3

import random as ran


class Dice:

    def __init__(self, number_of_sides=6):
        self.__number_of_sides = number_of_sides

    def roll(self):
        return ran.randint(1, self.__number_of_sides)

    def __str__(self):
        return f"Toto je kostka s {self.__number_of_sides} stenami"

    def getNum_of_sides(self):
        return self.__number_of_sides

    def setNum_of_sides(self, number_of_sides):
        if number_of_sides > 0:
            self.__number_of_sides = number_of_sides
        else:
            print("Cislo musi byt kladne")

    def setNum_of_sides_man(self):
        try:
            number_of_sides = int(input("Insert a number:"))
            if number_of_sides > 0:
                self.__number_of_sides = number_of_sides
            else:
                print("Zadej cislo vetsi nez 0")
        except:
            print("Zadani musi byt kladne cislo")


if __name__ == "__main__":
    pass