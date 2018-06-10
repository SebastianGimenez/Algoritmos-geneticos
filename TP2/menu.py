import tp2_heuristico as heuristico
import tp2_exhaustivo as exhaustivo
import sys

option = 99
while option != 0:
    print('Menu')
    print('1- Exhaustivo')
    print('2- Heuristico')
    print('3- Exhaustivo - variante')
    print('4- Heuristico - variante')
    print('')
    print('0- Salir')

    print('')
    option = int(input('Ingrese la opcion seleccionada: '))
    print('')

    if option == 1:
        exhaustivo.correr()
    if option == 2:
        heuristico.correr()
    if option == 3:
        exhaustivo.correr(True)
    if option == 4:
        heuristico.correr(True)

    print('')
    print('')
    input("Presione enter para repetir...")
