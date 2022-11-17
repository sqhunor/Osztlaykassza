from functions import *

choice = ''
while choice != '0':
    loadNameList()
    choice = menu()
    if choice == '1':
        addMoney()
    elif choice == '2':
        showNameList()
    elif choice == '3':
        pass
    elif choice == '4':
        pass