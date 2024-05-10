#!/usr/bin/env python3

lines = int(input('Enter the number of lines: '))
columns = int(input('Enter the number of columns: '))

tabulka = []
radek = []

for s in range(1, lines+1):
    for r in range(1, columns+1):
        hodnota = input(f'Zadej hodnotu pro {r}, sloupec a {s} radek: ')
        radek.append(hodnota)
    tabulka.append(radek)
    radek = []
print(tabulka)

f = open('tabulka.csv', 'w')
for line in tabulka:
    zapis = ''
    for column in line:
        zapis = zapis + column + ';'
    f.writelines(zapis)
    f.write('\n')

f.close()