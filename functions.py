from os import system
def menu():
    system('cls')  
    print('0 - Kilép')
    print('1 - Befizetés')
    print('2 - Névsor')
    print('3 - Legutóbbi befizetés/kiadás')
    print('4 - Számlán lévő egyenleg')
    return input('Választás:')