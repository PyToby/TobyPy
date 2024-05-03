#!/usr/bin/env python3

from bojovnik import Bojovnik
from kostka import Dice


class Mag(Bojovnik):
    def __init__(self, jmeno, zivot, utok, obrana, kostka, mana, magicky_utok):
        super().__init__(jmeno, zivot, utok, obrana, kostka)
        self._mana = mana
        self._max_mana = mana
        self._magicky_utok = magicky_utok

    def utoc(self, souper):
        if self._mana < self._max_mana:
            self._mana = self._mana + 10
            if self._mana > self._max_mana:
                self._max_mana = self._mana
            super().utoc(souper)
        else:
            uder = self._magicky_utok + self._kostka.roll()
            zprava = f'{self._jmeno} utoci magii za {uder}hp.'
            self.nastav_zpravu(zprava)
            self._mana = 0
            souper.bran_se(uder)

    def graficka_mana(self):
        return self.graficky_ukazatel(self._mana, self._max_mana)


class Arena():
    def __init__(self, bojovnik1, bojovnik2, kostka):
        self._bojovnik1 = bojovnik1
        self._bojovnik2 = bojovnik2
        self._kostka = kostka

    def _vykresli(self):
        self._vycisti()
        print("__________________ARENA__________________ \n")
        print('Bojovnici: \n')
        self._vypis_bojovnika(self._bojovnik1)
        self._vypis_bojovnika(self._bojovnik2)


    def _vycisti(self):
        import os as _os
        _os.system('cls' if _os.name == 'nt' else 'clear')

    def _vypis_zpravu(self, zprava):
        import time as _tm
        print(zprava)
        _tm.sleep(1)

    def zapas(self):
        import random as _ran
        print('Vitejte v Arene')
        print(f'Dnes se utkaji bojovnici {self._bojovnik1} a {self._bojovnik2}')
        print('Zapas muze zacit...', end=' ')
        input()

        if _ran.randint(0, 1):
            self._bojovnik1, self._bojovnik2 = self._bojovnik2, self._bojovnik1

        while self._bojovnik1.je_nazivu() and self._bojovnik2.je_nazivu():
            self._bojovnik1.utoc(self._bojovnik2)
            self._vykresli()
            self._vypis_zpravu(self._bojovnik1.vypis_zpravu())
            self._vypis_zpravu(self._bojovnik2.vypis_zpravu())
            if self._bojovnik2.je_nazivu():
                self._bojovnik2.utoc(self._bojovnik1)
                self._vykresli()
                self._vypis_zpravu(self._bojovnik1.vypis_zpravu())
                self._vypis_zpravu(self._bojovnik2.vypis_zpravu())

    def _vypis_bojovnika(self, bojovnik):
        print(bojovnik)
        print(f'Zivot: {bojovnik.grafic_zivot()}')
        if isinstance(bojovnik, Mag):
            print(f'Mana: {bojovnik.graficka_mana()}')


kostka = Dice(10)
bojovnik = Bojovnik("Eragon", 100, 20, 10, kostka)
souper = Bojovnik('Shadow', 80, 30, 15, kostka)
mag = Mag('Gandalf', 50, 15, 30, kostka, 30, 45)

a = Arena(mag, souper, kostka)
a.zapas()
