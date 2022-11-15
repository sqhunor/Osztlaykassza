from os import system
from data import * 

def menu():
    system('cls')  
    print('0 - Kilép')
    print('1 - Befizetés')
    print('2 - Névsor')
    print('3 - Legutóbbi befizetés/kiadás')
    print('4 - Számlán lévő egyenleg')
    return input('Választás:')

def  showNameList():
    system('cls')
    print('Versenyzők')
    for nev in nevsor:
        print(f'\t{nev}')
    input()
