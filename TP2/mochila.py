

class Mochila():

    def __init__(self, variante = False):
        self.capacidad = 4200
        if variante:
            self.capacidad = 3000

        self.volumen_acumulado = 0
        self.valor_acumulado = 0
        self.items = []

    def volumen_disponible(self):
        return self.capacidad - self.volumen_acumulado

    def agregar_objetos(self, obj_array, no_validar = False):
        for o in obj_array:
            if o.volumen <= self.volumen_disponible() or no_validar:
                self.items.append(o)
                self.volumen_acumulado = self.volumen_acumulado + o.volumen
                self.valor_acumulado = self.valor_acumulado + o.valor

    def informe_objetos(self):
        for o in self.items:
            print("Id: ", o.id,"Volumen: ", o.volumen, "Valor: ", o.valor)

        print("Valor en la mochila: ", self.valor_acumulado)
        print("Volumen: ", self.volumen_acumulado)