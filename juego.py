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


"""
def crea_tablero(fila, columna):
    matriz = []
    for i in range(fila):
        matriz.append([0]*columna)
    return matriz

def juega(tablero, columna, jugador):
    
    Realiza la jugada del jugador en la columna dada
    '''
    for fila in range(len(tablero) - 1, -1, -1):
        if tablero[fila][columna] == 0:
            tablero[fila][columna] = jugador
            return True  
    return False

def esta_llena(tablero, columna):
    '''
    seleccionar la columna que queremos comprobar (columna)
    comprobar si la columna tiene huecos con un in 
    devolver True o False
    '''
    c = tablero[columna]  
    return 0 not in c

def victoria_vertical_col(tablero, pos_columna, ficha):
    contador_iguales = 0
    columna = tablero[pos_columna]

    ix = 0
    while ix < len(columna):
        if columna[ix] == ficha:
            contador_iguales += 1
        else:
            contador_iguales = 0

        ix += 1
        if contador_iguales == 4:
            return True

    return False

def victoria(tablero, ficha):
    '''
    Obtener el numero de columnas de mi tablero
    iterar sobre range(num_columnas)
        para cada columna si es True devolver True
        si es False ir a la siguiente

    Si salgo del bucle, devolver false
    '''
    num_cols = len(tablero)
    for num_col in range(num_cols):
        if victoria_vertical_col(tablero, num_col, ficha):
            return True
        
    return False

def victoria_horizontal_fila(tablero,pos_fila,ficha):
    contador_iguales = 0
    
    for columna in tablero:
        if columna[pos_fila] == ficha:
            contador_iguales += 1
        else:
            contador_iguales = 0

        if contador_iguales == 4:
            return True
    return False
"""