#!/usr/bin/env python3

import csv

def read_csv_file(filename):
    rows = []

    with open(filename, 'r', newline='', encoding='utf-8') as file:
        csv_reader = csv.reader(file, delimiter = ';')
        for line in csv_reader:
            rows.append(line)
        
        return rows

if __name__ == '__main__':
    csv_file = 'data.csv'
    csv_data = read_csv_file(csv_file)
    
    #print(csv_data[1][1]) upresneni na 1. radek a 1. sloupec

    for r, row in enumerate(csv_data, 0): #bez zavorek
        print(r,'', end='')
        for column in row:
            print(f'{column};', end='')
        print('')