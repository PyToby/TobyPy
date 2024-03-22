#!/usr/bin/env python3

"""
Bojovnik
"""


class Bojovnik():
    """
    Class reprezntujici bojovnika do areny.
    """

    def __init__(self, jmeno, zivot, utok, obrana, kostka):
        self._jmeno = jmeno
        self._zivot = zivot
        self._max_zivot = zivot
        self._utok = utok
        self._obrana = obrana
        self._kostka = kostka

    def __str__(self):
        return str(self._jmeno)

    def je_nazivu(self):
        if self._zivot > 0:
            return True
        else:
            return False

    def grafic_zivot(self):
        celkem = 20
        pocet = int(self._zivot / self._max_zivot * celkem)
        if pocet == 0 and self.je_nazivu():
            pocet = 1
        return f"[{'#'* pocet}{' ' * (celkem - pocet)}]"

