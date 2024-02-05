def tablero(fila, columna):
    """
    Crea un tablero donde con valores iniciales a 0
    """
    matriz = []
    for i in range(fila):
        matriz.append([0]*columna)
    return matriz

def dibujar(element):
    """
    Imprime el tablero como una lista de filas
    """
    for i in element:
        print(i)

salida = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
]

assert tablero(6, 7) == salida # prueba y error

teblero = tablero(6,7)


def juega(columna,jugador):
    pass

def busca_hueco(columna):
    pass