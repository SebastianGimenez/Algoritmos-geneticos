
class Objeto():
    id = None
    volumen = None
    valor = None

    def __init__(self, id, volumen, valor):
        self.id = id
        self.volumen = volumen
        self.valor = valor
        self.indice = self.valor / self.volumen


