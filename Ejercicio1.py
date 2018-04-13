import random
import xlwt

a = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

#arreglo poblacion inicial
def generarPoblacionInicial(a):
    for i in range(10):
        for j in range(30):
            a[i][j] = random.randint(0,1)
    return a


#genera arreglo con decimales
def getDecimal(arreglo):
    numerosDecimales=[]
    for i in range (10):
        numero=0
        for indice , num in enumerate(arreglo[i][::-1]):
            numero = numero + (2**indice) * num
        numerosDecimales.append(numero)
    return(numerosDecimales)


#define funcion objetivo
def objetivo(x):
    return (x/((2**30)-1))**2

#genera arreglo con los valores de la funcion objetivo
def getObjetivos(decimales):
    objetivos=[]
    for elemento in decimales:
        objetivos.append(objetivo(elemento))
    return objetivos



#genera arreglo de fitness
def getFitness(objetivos):
    fitness = []
    for e in objetivos:
        fitness.append(e/sum(objetivos))
    return fitness


#generar acumulado
def getAcumulado(fitness):
    acumulado = []
    for n in range(10):
        suma = 0
        for i in range(n+1):
            suma = suma + fitness[i]
        acumulado.append(suma)
    return acumulado


#seleccion de cromosomas
def seleccionarCromosoma(acumulado):
    ran=random.random()
    for index, n in enumerate(acumulado):
        if ran < n:
            return index


#funcion de crossover
def crossover(crom1,crom2):
    prob=random.random()
    if prob<=0.75:
        corte=random.randint(0,29)
        parteIntercambiale=crom1[corte:]
        j=0
        for i in range(corte, 29):
            crom1[i]=crom2[i]
            crom2[i]=parteIntercambiale[j]
            j=j+1
        return crom1,crom2
    else: return crom1,crom2

#mutacion
def mutacion(crom):
    prob=random.random()
    if prob<=0.05:
        gen=random.randint(0,29)
        if crom[gen]==0:
            crom[gen]=1
        else:
            crom[gen]=0
        return crom
    else: return crom





a=generarPoblacionInicial(a)
#generar el excel
style0 = xlwt.easyxf('font: name Times New Roman, colour black, bold on')
wb = xlwt.Workbook()
ws = wb.add_sheet('Ejercicio1',cell_overwrite_ok=True)
ws.write(0,0,'maximos',style0)
ws.write(0,1,'minimos',style0)
ws.write(0,2,'promedios',style0)
ws.write(0,3,'cromosomas',style0)
for i in range(20):
    decimales=getDecimal(a)
    objetivos=getObjetivos(decimales)
    fitness=getFitness(objetivos)
    acumulado=getAcumulado(fitness)
    maximo=max(objetivos)
    minimo=min(objetivos)
    indiceMax=objetivos.index(max(objetivos))
    prom_obj = sum(objetivos)/len(objetivos)
    ws.write(i+1,0,maximo,style0)
    ws.write(i+1,1,minimo,style0)
    ws.write(i+1,2,prom_obj,style0)
    ws.write(i+1,3,str(a[indiceMax]),style0)
    cromosoma=[]
    for k in range(10):
        cromosoma.append(seleccionarCromosoma(acumulado))
    a[cromosoma[0]],a[cromosoma[1]]=crossover(a[cromosoma[0]],a[cromosoma[1]])
    a[cromosoma[2]],a[cromosoma[3]]=crossover(a[cromosoma[2]],a[cromosoma[3]])
    a[cromosoma[4]],a[cromosoma[5]]=crossover(a[cromosoma[4]],a[cromosoma[5]])
    a[cromosoma[6]],a[cromosoma[7]]=crossover(a[cromosoma[6]],a[cromosoma[7]])
    a[cromosoma[8]],a[cromosoma[9]]=crossover(a[cromosoma[8]],a[cromosoma[9]])
    for j in range(10):
        a[cromosoma[j]]=mutacion(a[cromosoma[j]])
wb.save('algGen')
