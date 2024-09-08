#!/usr/bin/env python3

cinnonst = 'cteni'
if cinnonst == 'cteni':
    f = open('test', 'r')
    obsah = f.read()
    for char in obsah:
        print(char)

    #print(obsah)
    #print(obsah[0].strip)  #strip znici prvni a posledni bily znaky = mezery
    #print(obsah[1])

elif cinnonst == 'zapis':
    f = open('test', 'w')
    f.write('Hello world!\n')
    f.write('another line')
    f.close()

