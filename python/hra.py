#!/usr/bin/env python3

import kostka

k = kostka.Dice(10)

print(f"Kostka ma {k.number_of_sides} sten")
print(f"Na kostce padlo: {k.roll()}")