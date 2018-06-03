import random
import xlwt


cant_corridas = 100


# arreglo poblacion inicial
def generarPoblacionInicial(a):
    for i in range(10):
        for j in range(30):
            a[i][j] = random.randint(0, 1)
    return a


# genera arreglo con decimales
def getDecimal(arreglo):
    numerosDecimales = []
    for i in range(10):
        numero = 0
        for indice, num in enumerate(arreglo[i][::-1]):
            numero = numero + (2**indice) * num
        numerosDecimales.append(numero)
    return numerosDecimales


# define funcion objetivo
def objetivo(x):
    return (x/((2**30)-1))**2


# genera arreglo con los valores de la funcion objetivo
def getObjetivos(decimales):
    objetivos = []
    for elemento in decimales:
        objetivos.append(objetivo(elemento))
    return objetivos


# genera arreglo de fitness
def getFitness(objetivos):
    fitness = []
    suma = sum(objetivos)
    for e in objetivos:
        fitness.append(e/suma)
    return fitness


# generar acumulado
def getAcumulado(fitness):
    acumulado = []
    for n in range(10):
        suma = 0
        for i in range(n+1):
            suma = suma + fitness[i]
        acumulado.append(suma)
    return acumulado


# seleccion de cromosomas
def seleccionarCromosoma(acumulado):
    ran = random.random()
    for index, n in enumerate(acumulado):
        if ran < n:
            return index


# funcion de crossover
def crossover(crom1, crom2):
    prob = random.random()
    if prob <= 0.75:
        corte = random.randint(0, 29)
        parteIntercambiale = crom1[corte:]
        j = 0
        for i in range(corte, 29):
            crom1[i] = crom2[i]
            crom2[i] = parteIntercambiale[j]
            j = j+1
        return crom1, crom2
    else:
        return crom1, crom2


# mutacion
def mutacion(crom, corrida):
    prob = random.random()
    # corrida.hubo_mutacion = False
    if prob <= 0.05:
        # corrida.hubo_mutacion = True
        gen = random.randint(0, 29)
        if crom[gen] == 0:
            crom[gen] = 1
        else:
            crom[gen] = 0
        return crom
    else:
        return crom


class Corrida:
    pass


# genera archivo .xls con información de cada corrida
def generarExcel(corridas):
    style0 = xlwt.easyxf('font: name Times New Roman, colour black, bold on')
    wb = xlwt.Workbook()
    ws = wb.add_sheet('Ejercicio1', cell_overwrite_ok=True)
    ws.write(0, 0, 'Máximos', style0)
    ws.write(0, 1, 'Mínimos', style0)
    ws.write(0, 2, 'Promedios', style0)
    ws.write(0, 3, 'Cromosomas', style0)
    i = 0
    for corrida in corridas:
        ws.write(i + 1, 0, corrida.maximo, style0)
        ws.write(i + 1, 1, corrida.minimo, style0)
        ws.write(i + 1, 2, corrida.prom_obj, style0)
        ws.write(i + 1, 3, str(corrida.poblacion[corrida.indiceMax]), style0)
        print(corrida.poblacion)
        i = i + 1
        wb.save('algGen.xls')


# programa principal

a = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], ]
a = generarPoblacionInicial(a)
corridas = []
style0 = xlwt.easyxf('font: name Times New Roman, colour black, bold on')
wb = xlwt.Workbook()
ws = wb.add_sheet('Ejercicio1', cell_overwrite_ok=True)
ws.write(0, 0, 'Máximos', style0)
ws.write(0, 1, 'Mínimos', style0)
ws.write(0, 2, 'Promedios', style0)
ws.write(0, 3, 'Cromosomas', style0)
ws.write(0, 4, 'Mutación', style0)

for i in range(cant_corridas):
    corrida = Corrida()
    corrida.decimales = getDecimal(a)
    corrida.objetivos = getObjetivos(corrida.decimales)
    corrida.fitness = getFitness(corrida.objetivos)
    corrida.acumulado = getAcumulado(corrida.fitness)
    corrida.maximo = max(corrida.objetivos)
    corrida.objetivos2 = corrida.objetivos
    corrida.objetivos2.remove(corrida.maximo)
    corrida.maximo2 = max(corrida.objetivos2)
    corrida.minimo = min(corrida.objetivos)
    corrida.indiceMax = corrida.objetivos.index(max(corrida.objetivos))
    corrida.indiceMax2 = corrida.objetivos.index(max(corrida.objetivos2))
    corrida.prom_obj = sum(corrida.objetivos) / len(corrida.objetivos)


    cromosoma = []
    cromosoma.append(corrida.indiceMax)
    cromosoma.append(corrida.indiceMax2)
    for k in range(8):
        cromosoma.append(seleccionarCromosoma(corrida.acumulado))
    a[cromosoma[2]], a[cromosoma[3]] = crossover(a[cromosoma[2]], a[cromosoma[3]])
    a[cromosoma[4]], a[cromosoma[5]] = crossover(a[cromosoma[4]], a[cromosoma[5]])
    a[cromosoma[6]], a[cromosoma[7]] = crossover(a[cromosoma[6]], a[cromosoma[7]])
    a[cromosoma[8]], a[cromosoma[9]] = crossover(a[cromosoma[8]], a[cromosoma[9]])

    for j in range(2,10):
        a[j] = mutacion(a[j], corrida)
    corrida.poblacion = list(a)

    ws.write(i + 1, 0, corrida.maximo, style0)
    ws.write(i + 1, 1, corrida.minimo, style0)
    ws.write(i + 1, 2, corrida.prom_obj, style0)
    ws.write(i + 1, 3, str(a[corrida.indiceMax]), style0)
    # ws.write(i + 1, 4, "Si" if corrida.hubo_mutacion else "No")
    print(corrida.poblacion)

    corridas.append(corrida)
wb.save('algGenB.xls')
# generarExcel(corridas)
