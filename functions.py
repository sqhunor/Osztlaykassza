from os import system
from data import * 

nevek = []
osszegek = []


filename= 'data.csv'


def menu():
    system('cls')  
    print('0 - Kilép')
    print('1 - Befizetés')
    print('2 - Névsor')
    print('3 - Legutóbbi befizetés/kiadás')
    print('4 - Számlán lévő egyenleg')
    return input('Választás:')

def loadNameList():
    file = open(filename, 'r', encoding='utf-8 ')
    global cimsor
    global nevek
    cimsor = file.readline()
    for row in file:
        splitted = row.strip().split(';')
        nevek.append(splitted[0])
        osszegek.append(splitted[1])
    file.close()
    
def  showNameList():
    system('cls')
    print('Névsor:')
    file = open
    
    input()

def addMoney():
    system('cls')
    print('Befizetés:')
    nev = input('Név:')
    osszeg = float(input('Összeg:'))
    pass
