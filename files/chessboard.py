#!/usr/bin/env python3


def num_fields():
    for num in range(1, 65):
        if num == 64:
            print(f'{num}.')
        else:
            print(f'{num}, ', end='')

if __name__ == '__main__':
    num_fields()
