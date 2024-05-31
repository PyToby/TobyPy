#!/usr/bin/env python3


def num_row():
    for field in range(1, 65):
        if field == 64:
            print(f'{field}.')
        else:
            print(f'{field}, ', end='')

def num_field():
    fields = range(1, 65)
    for row in range(1, 9):
        for columns in range(1, 9):
            print(fields[columns-1], end='')
        print()

if __name__ == '__main__':
    num_field()
