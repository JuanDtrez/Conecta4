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

def busca_hueco(tablero, columna):
    """
    Busca la primera fila vacía en la columna dada
    """
    for fila in range(len(tablero) - 1, -1, -1):
        if tablero[fila][columna] == 0:
            return fila
    return None  # Columna llena

def juega(tablero, columna, jugador):
    """
    Realiza la jugada del jugador en la columna dada
    """
    for fila in range(len(tablero) - 1, -1, -1):
        if tablero[fila][columna] == 0:
            tablero[fila][columna] = jugador
            return True  
    return False  

# Tamaño del tablero
tablero = tablero(6, 7)

# Jugada 1
juega(tablero, 3, 1)

# Jugada 2
juega(tablero, 3, 2)

# Aplicar el formato de tabla
dibujar(tablero)
