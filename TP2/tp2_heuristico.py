import time

import mochila as mochila_module
import objeto as objeto_module



def obtener_arreglo_inicial(variante = False):
    arreglo_inicial = []
    arreglo_inicial.append(objeto_module.Objeto(1, 150, 20))
    arreglo_inicial.append(objeto_module.Objeto(2, 325, 40))
    arreglo_inicial.append(objeto_module.Objeto(3, 600, 50))
    arreglo_inicial.append(objeto_module.Objeto(4, 805, 36))
    arreglo_inicial.append(objeto_module.Objeto(5, 430, 25))
    arreglo_inicial.append(objeto_module.Objeto(6, 1200, 64))
    arreglo_inicial.append(objeto_module.Objeto(7, 770, 54))
    arreglo_inicial.append(objeto_module.Objeto(8, 60, 18))
    arreglo_inicial.append(objeto_module.Objeto(9, 930, 46))
    arreglo_inicial.append(objeto_module.Objeto(10, 353, 28))

    arreglo_variante = []

    arreglo_variante.append(objeto_module.Objeto(1, 1800, 72))
    arreglo_variante.append(objeto_module.Objeto(2, 600, 36))
    arreglo_variante.append(objeto_module.Objeto(3, 1200, 60))

    if variante:
        return arreglo_variante

    return arreglo_inicial



def correr(variante = False):
    # Guardar el tiempo al inicio
    start = time.time()

    # Ordenar por el indice que utilizamos como criterio
    ordenado = sorted(obtener_arreglo_inicial(variante), key=lambda obj: obj.indice, reverse=True)

    for i in ordenado:
        print(i.indice)
        print(i.volumen)
        print(i.valor)
    # Crear objeto mochila
    mochila = mochila_module.Mochila(variante)

    # Agregarle objetos hasta que se llene
    mochila.agregar_objetos(ordenado)

    # Guardar el tiempo al final
    end = time.time()

    # Informe de resultados
    print("Tiempo de resolucion: ", (end - start), "segundos")
    mochila.informe_objetos()