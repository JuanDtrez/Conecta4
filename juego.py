def dibujar(element):
    for i in element:
        print(i)

def tablero(fila, columna):
    matriz = []
    for i in range(fila):
        matriz.append([0]*columna)
    return matriz

salida = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
]

assert tablero(6, 7) == salida

print(dibujar(tablero(6,7)))

