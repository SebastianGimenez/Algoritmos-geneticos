import copy
import random

capitales = ['Buenos Aires',
             'Cordoba',
             'Corrientes',
             'Formosa',
             'La Plata',
             'La Rioja',
             'Mendoza',
             'Neuquen',
             'Parana',
             'Posadas',
             'Rawson',
             'Resistencia',
             'Rio Gallegos',
             'S. F. d. V. d. Catamarca',
             'S. M. de Tucuman',
             'S. S. de Jujuy',
             'Salta',
             'San Juan',
             'San Luis',
             'Santa Fe',
             'Santa Rosa',
             'Sgo. Del Estero',
             'Ushuaia',
             'Viedma']

distancias = [[
        0, 646, 792, 933, 53, 986, 985, 989, 375, 834, 1127, 794, 2082, 979, 1080, 1334, 1282, 1005, 749, 393, 579, 939, 2373, 799
    ],[
        646, 0, 677, 824, 698, 340, 466, 907, 348, 919, 1321, 669, 2281, 362, 517, 809, 745, 412, 293, 330, 577, 401, 2618, 1047
    ],[
        792, 677, 0, 157, 830, 814, 1131, 1534, 500, 291, 1845, 13, 2819, 691, 633, 742, 719, 1039, 969, 498, 1136, 535, 3131, 1527
    ],[
        933, 824, 157, 0, 968, 927, 1269, 1690, 656, 263, 1999, 161, 2974, 793, 703, 750, 741, 1169, 1117, 654, 1293, 629, 3284, 1681
    ],[
        53, 698, 830, 968, 0, 1038, 1029, 1005, 427, 857, 1116, 833, 2064, 1030, 1132, 1385, 1333, 1053, 795, 444, 602, 991, 2350, 789
    ],[
        986, 340, 814, 927, 1038, 0, 427, 1063, 659, 1098, 1548, 802, 2473, 149, 330, 600, 533, 283, 435, 640, 834, 311, 2821, 1311
    ],[
        985, 466, 1131, 1269, 1029, 427, 0, 676, 790, 1384, 1201, 1121, 2081, 569, 756, 1023, 957, 152, 235, 775, 586, 713, 2435, 1019
    ],[
        989, 907, 1534, 1690, 1005, 1063, 676, 0, 1053, 1709, 543, 1529, 1410, 1182, 1370, 1658, 1591, 824, 643, 1049, 422, 1286, 1762, 479
    ],[
        375, 348, 500, 656, 427, 659, 790, 1053, 0, 658, 1345, 498, 2320, 622, 707, 959, 906, 757, 574, 19, 642, 566, 2635, 1030
    ],[
        834, 919, 291, 263, 857, 1098, 1384, 1709, 658, 0, 1951, 305, 2914, 980, 924, 1007, 992, 1306, 1200, 664, 1293, 827, 3207, 1624
    ],[
        1127, 1321, 1845, 1999, 1116, 1548, 1201, 543, 1345, 1951, 0, 1843, 975, 1647, 1827, 2120, 2054, 1340, 1113, 1349, 745, 1721, 1300, 327
    ],[
        794, 669, 13, 161, 833, 802, 1121, 1529, 498, 305, 1843, 0, 2818, 678, 620, 729, 706, 1029, 961, 495, 1132, 523, 3130, 1526
    ],[
        2082, 2281, 2819, 2974, 2064, 2473, 2081, 1410, 2320, 2914, 975, 2818, 0, 2587, 2773, 3063, 2997, 2231, 2046, 2325, 1712, 2677, 359, 1294
    ],[
        979, 362, 691, 793, 1030, 149, 569, 1182, 622, 980, 1647, 678, 2587, 0, 189, 477, 410, 430, 540, 602, 915, 166, 2931, 1391
    ],[
        1080, 517, 633, 703, 1132, 330, 756, 1370, 707, 924, 1827, 620, 2773, 189, 0, 293, 228, 612, 727, 689, 1088, 141, 3116, 1562
    ],[
        1334, 809, 742, 750, 1385, 600, 1023, 1658, 959, 1007, 2120, 729, 3063, 477, 293, 0, 67, 874, 1017, 942, 1382, 414, 3408, 1855
    ],[
        1282, 745, 719, 741, 1333, 533, 957, 1591, 906, 992, 2054, 706, 2997, 410, 228, 67, 0, 808, 950, 889, 1316, 353, 3341, 1790
    ],[
        1005, 412, 1039, 1169, 1053, 283, 152, 824, 757, 1306, 1340, 1029, 2231, 430, 612, 874, 808, 0, 284, 740, 686, 583, 2585, 1141
    ],[
        749, 293, 969, 1117, 795, 435, 235, 643, 574, 1200, 1113, 961, 2046, 540, 727, 1017, 950, 284, 0, 560, 412, 643, 2392, 882
    ],[
        393, 330, 498, 654, 444, 640, 775, 1049, 19, 664, 1349, 495, 2325, 602, 689, 942, 889, 740, 560, 0, 641, 547, 2641, 1035
    ],[
        579, 577, 1136, 1293, 602, 834, 586, 422, 642, 1293, 745, 1132, 1712, 915, 1088, 1382, 1316, 686, 412, 641, 0, 977, 2044, 477
    ],[
        939, 401, 535, 629, 991, 311, 713, 1286, 566, 827, 1721, 523, 2677, 166, 141, 414, 353, 583, 643, 547, 977, 0, 3016, 1446
    ],[
        2373, 2618, 3131, 3284, 2350, 2821, 2435, 1762, 2635, 3207, 1300, 3130, 359, 2931, 3116, 3408, 3341, 2585, 2392, 2641, 2044, 3016, 0, 1605
    ],[
        799, 1047, 1527, 1681, 789, 1311, 1019, 479, 1030, 1624, 327, 1526, 1294, 1391, 1562, 1855, 1790, 1141, 882, 477, 1446, 1605, 0
]]

arreglo_inicial=[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]



#########################  Algoritmo Genetico  ##########################

#funcion de generacion de poblacion inicial
def gen_pob_ini(a):
    for i in range(50):
        for j in range(24):
            bandera = True
            while bandera:
                num = random.randint(0, 24)
                if num not in a[i]:
                    a[i][j] = num
                    bandera = False
    for i in range(50):
        for j in range(24):
            a[i][j]=a[i][j]-1
    return a

#funcion objetivo
def funcion_objetivo(a,distancias):
    obj=[]
    for i in range(50):
        sum=0
        for j in range(23):
            #print(a[i][j],a[i][j+1])
            #print(distancias[a[i][j]][a[i][j+1]])
            sum = sum + distancias[a[i][j]][a[i][j+1]]
            #print(sum)
        sum = sum + distancias[a[i][23]][a[i][0]]
        obj.append(sum)
    return obj


#funcion fitness
def fitness(obj):
    total=sum(obj)
    #print(total)
    fitness=[None]*50
    for i in range(50):
        fitness[i] = 1-(obj[i]/total)
    #print(fitness)
    total2=sum(fitness)
    for i in range(50):
        fitness[i] = (fitness[i]/total2)
    #print(fitness)
    return fitness

#acumulado
def acumulado(fitness):
    acumulado = []
    for n in range(50):
        suma = 0
        for i in range(n+1):
            suma = suma + fitness[i]
        acumulado.append(suma)
    return acumulado

#sleccion
def seleccionarCromosoma(acumulado):
    ran = random.random()
    for index, n in enumerate(acumulado):
        if ran < n:
            return index

# funcion de crossover
def crossover(crom1, crom2):
    prob = random.random()
    if prob <= 0.75:
        crom_nuevo_1 = [None]*24
        crom_nuevo_2 = [None]*24
        i = 0
        crom_nuevo_1[i] = crom1[i]
        while((crom2[i] in crom1) & (crom2[i] not in crom_nuevo_1)):
            i = crom1.index(crom2[i])
            crom_nuevo_1[i] = crom1[i]
        for gen in crom2:
            if(crom_nuevo_1[crom2.index(gen)] is None):
                crom_nuevo_1[crom2.index(gen)] = gen
        i = 0
        crom_nuevo_2[i] = crom2[i]
        while((crom1[i] in crom2) & (crom1[i] not in crom_nuevo_2)):
            i = crom2.index(crom1[i])
            crom_nuevo_2[i] = crom2[i]
        for gen in crom1:
            if(crom_nuevo_2[crom1.index(gen)] is None):
                crom_nuevo_2[crom1.index(gen)] = gen
        return crom_nuevo_1,crom_nuevo_2
    else:
        return crom1, crom2

def mutacion(crom):
    prob = random.random()
    if prob <= 0.05:
        gen1 = random.randint(0, 23)
        gen2 = gen1
        while gen2 == gen1:
            gen2 = random.randint(0, 23)
        gen = crom[gen1]
        crom[gen1] = crom[gen2]
        crom[gen2] = gen
        return crom
    else:
        return crom






#principal geneticos
def geneticos_resolucion():
    a=gen_pob_ini(arreglo_inicial)


    for i in range(200):
        obj = funcion_objetivo(a, distancias)
        fitness_ = fitness(obj)
        acumulado_ = acumulado(fitness_)
        indices_seleccionados = []

        #####  ANTERIOR  ########
        # for i in range(50):
        #    indices_seleccionados.append(seleccionarCromosoma(acumulado_))
        # nueva_pob=copy.deepcopy(arreglo_inicial)
        # for i in range(0,50,2):
        #  nueva_pob[i],nueva_pob[i+1] = crossover(a[indices_seleccionados[i]],a[indices_seleccionados[i+1]])
        # for j in range(50):
        #    nueva_pob[j] = mutacion(nueva_pob[j])

        ###########################

        ##########  ELITISMO    ##############
        maximo1=max(obj)
        obj2 = obj
        obj2.remove(maximo1)
        maximo2=max(obj2)
        obj3=obj2
        obj3.remove(maximo2)
        maximo3=max(obj3)
        obj4=obj3
        obj4.remove(maximo3)
        maximo4=max(obj4)
        indiceMax1=obj.index(max(obj))
        indiceMax2=obj.index(max(obj2))
        indiceMax3 = obj.index(max(obj3))
        indiceMax4 = obj.index(max(obj4))
        indices_seleccionados.append(indiceMax1)
        indices_seleccionados.append(indiceMax2)
        indices_seleccionados.append(indiceMax3)
        indices_seleccionados.append(indiceMax4)

        for i in range(46):
            indices_seleccionados.append(seleccionarCromosoma(acumulado_))
        nueva_pob=copy.deepcopy(arreglo_inicial)
        for i in range(4, 50, 2):
         nueva_pob[i],nueva_pob[i+1] = crossover(a[indices_seleccionados[i]],a[indices_seleccionados[i+1]])
        for j in range(4,50):
            nueva_pob[j] = mutacion(nueva_pob[j])

        ################ FIN DE ELITISMO  ##################

        a = copy.deepcopy(nueva_pob)
    menor_nueva_pob=min(nueva_pob)
    for i in range(24):
        print(capitales[menor_nueva_pob[i]])
    print(fitness_)
    print(acumulado_)
    print(obj)





########################### Heuristico ###################################

def buscaRuta(capitalini,imprimir = False):
    capital_inicial = capitales.index(capitalini)
    recorrido = [capital_inicial]

    capital_actual = capital_inicial

    distancias_actual = copy.deepcopy(distancias[capital_actual])

    dist_total = 0
    while recorrido.__len__() != capitales.__len__():
        dist_minima = 1000000
        for i in range(0, distancias_actual.__len__()):
            dist = distancias_actual[i]
            if dist < dist_minima and i not in recorrido:
                dist_minima = dist
                ind_minimo = i

        dist_total += dist_minima
        recorrido.append(ind_minimo)
        distancias_actual = copy.deepcopy(distancias[ind_minimo])

    recorrido.append(capital_inicial)
    dist_total += distancias[ind_minimo][capital_inicial]

    if(imprimir):
        print("Distancia total recorrida: ", dist_total)
        print("Recorrido:\n")
        for i in range(25):
            print(capitales[recorrido[i]])
    else:
        return [dist_total,recorrido]



# Principal

opcion1 = input("Seleccione una opcion:\n1-Heuristico\n2-Algoritmos Geneticos\n")
if (opcion1 == '1'):
    opcion = input("Seleccione una opcion:\n1-Ingresar ciudad de salida\n2-Elegir ciudad aleatoria\n3-Obtener menor ruta\n")
    if(opcion == '1'):
        capitalini = input("ingrese el nombre de la ciudad de salida: ")
        buscaRuta(capitalini,True)
    elif(opcion == '2'):
        capitalini = random.choice(capitales)
        buscaRuta(capitalini,True)
    elif(opcion == '3'):
        dist_min = 999999999999999
        for capital in capitales:
            busqueda = buscaRuta(capital)
            if(busqueda[0] < dist_min):
                dist_min = busqueda[0]
                recorrido = busqueda[1]
        print("Distancia minima: ",dist_min)
        print("Recorrido:\n")
        for i in range(25):
            print(capitales[recorrido[i]])
else:
    geneticos_resolucion()

