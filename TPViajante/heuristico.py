import copy

capitales = ['Buenos Aires',
             'Santa Fe',
             'Cordoba',
             'Tierra del Fuego']

distancias = [[
        0, 450, 800, 1800
    ],[
        450, 0, 400, 2200
    ],[
        800, 400, 0, 2300
    ],[
        1800, 2200, 2300, 0
]]

capital_inicial = 0
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
            dist_total += distancias[ind_minimo][i]
            ind_minimo = i
    recorrido.append(ind_minimo)
    distancias_actual = copy.deepcopy(distancias[ind_minimo])

recorrido.append(capital_inicial)
dist_total += distancias[ind_minimo][capital_inicial]

print(dist_total)
