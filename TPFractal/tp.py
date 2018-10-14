import matplotlib.pyplot as plt




def fractal(longitud = 150.0, y = 50, startx = 0):
    if longitud < 1:
        return None
    else:
        dibujar(longitud, y, startx)
        longitud = longitud / 3
        for j in [startx, startx + (longitud*2)]:
            fractal(longitud, y - 10, j)

def dibujar(longitud, y, startx):
    plt.plot([startx,startx+longitud],[y,y],'k-')
    pass



fractal()
plt.show()