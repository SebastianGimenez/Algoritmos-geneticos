import itertools
import copy
import time

import mochila as mochila_module
import objeto as objeto_module

def obtener_arreglo_inicial(variante = False):
    arreglo_inicial = []
    arreglo_inicial.append(objeto_module.Objeto(1, 150, 120))
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

    # Obtener arreglo inicial
    arreglo_inicial = obtener_arreglo_inicial(variante)

    # Inicializar
    valor_maximo = 0

    # Recorrer todas las combinaciones posibles de objetos y guardar la mochila que tiene el mejor valor
    for size in range(1, 11):
        for combinacion in itertools.combinations(arreglo_inicial, size):
            mochila = mochila_module.Mochila(variante)
            mochila.agregar_objetos(combinacion, True)
            if mochila.valor_acumulado > valor_maximo and mochila.volumen_disponible() >= 0:
                mejor_mochila = copy.copy(mochila)

    # Guardar el tiempo al final
    end = time.time()

    # Informe de resultados
    print("Tiempo de resolucion: ", (end - start), "segundos")
    mejor_mochila.informe_objetos()