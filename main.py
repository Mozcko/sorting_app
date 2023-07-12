import os
from PIL import Image



def main():
    menu()
    
def print_menu():
    
    os.system("clear")

    print(30 * "-" , "MENU" , 30 * "-")
    print("1. Sort Only")
    print("2. Sort and Compress images")
    print("3. Change folder to sort")
    print("4. Only sort Downloads folder")
    print("5. Exit")
    print(67 * "-")
    

def menu():
    running = True
    while running:
        print_menu()
        op = input('selecciona una opcion [1-5]: ')
        
        if op == '1':
            pass
        elif op == '2':
            pass
        elif op == '3':
            pass
        elif op == '4':
            pass
        elif op == '5':
            print("Good bye")
            running = False
        else:
            print('opcion no valida, por favor seleccione una opcion valida')
    



if __name__ == "__main__":
    main()
