#!/usr/bin/env python3

from bojovnik import Bojovnik
from kostka import Dice


class Arena():
    def __init__(self, bojovnik1, bojovnik2, kostka):
        self._bojovnik1 = bojovnik1
        self._bojovnik2 = bojovnik2
        self._kostka = kostka

    def _vykresli(self):
        self._vycisti()
        print("__________________ARENA__________________ \n")
        print('Zdravi bojovniku: \n')
        print(f'{self._bojovnik1} {self._bojovnik1.grafic_zivot()}')
        print(f'{self._bojovnik2} {self._bojovnik2.grafic_zivot()}')

    def _vycisti(self):
        import sys as _sys
        import subprocess as _subprocess
        if _sys.platform.startswith('win'):
            _subprocess.call(['cmd.exe', '/C', 'cls'])
        else:
            _subprocess.call(['clear'])

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


kostka = Dice(10)
bojovnik = Bojovnik("Eragon", 100, 20, 10, kostka)
souper = Bojovnik('Shadow', 80, 30, 15, kostka)

a = Arena(bojovnik, souper, kostka)
a.zapas()
