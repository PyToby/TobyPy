#!/usr/bin/env python3

from bojovnik import Bojovnik
from kostka import Dice

kostka = Dice(10)
bojovnik = Bojovnik("Eragon", 100, 20, 10, kostka)
print(f"Zivot: {bojovnik.grafic_zivot()}")
souper = Bojovnik('Shadow', 80, 1800, 15, kostka)
souper.utoc(bojovnik)
print(souper.vypis_zpravu())
print(bojovnik.vypis_zpravu())
print(f'Zivot: {bojovnik.grafic_zivot()}')