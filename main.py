from menu_options import read_from_file, testing_mode
from logic import find_solution

# Interfaz de usuario principal
def main():
    cities = []
    valid = False
    while not valid:
        valid = True
        print("1.- Leer distancias de un archivo")
        print("2.- Utilizar casos de prueba")
        print("0.- EXIT")
        option = int(input("Seleccione una opcion: "))
        if (option == 1):
            read_from_file()
        elif (option == 2):
            testing_mode()
        elif (option == 0):
            exit()
        else:
            print("Por favor seleccione una opción válida")
            valid = False
        

if (__name__ == "__main__"):
    main()

    