
def fractal(longitud = 150.0, y = 0, startx = 0):
    if longitud < 1:
        return None
    else:
        print(".-----------.")
        print(longitud)
        print(y)
        print(startx)
        dibujar(longitud, y, startx)
        longitud = longitud / 3
        for j in [startx, startx + (longitud*2)]:
            fractal(longitud, y + 10, j)

def dibujar(longitud, y, startx):
    pass


fractal()