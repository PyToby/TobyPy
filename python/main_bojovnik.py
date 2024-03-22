#!/usr/bin/env python3

from bojovnik import Bojovnik
from kostka import Dice

kostka = Dice(10)
bojovnik = Bojovnik("Eragon", 100, 20, 10, kostka)

print(f"Bojovnik: {bojovnik}")
print(f"Nazivu: {bojovnik.je_nazivu()}")
print(f"Zivot: {bojovnik.grafic_zivot()}")
