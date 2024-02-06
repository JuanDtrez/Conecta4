def crea_tablero(fila, columna):
    matriz = []
    for i in range(columna):
        matriz.append([0]*fila)
    return matriz

def juega(tablero, columna, ficha):
    """
    Realiza la jugada del jugador en la columna dada
    """
    c = tablero[columna]

    for indice in range(len(c) - 1, -1, -1):
        if c[indice] == 0:
            c[indice] = ficha
            break

def esta_llena(tablero, columna):
    """
    seleccionar la columna que queremos comprobar (columna)
    comprobar si la columna tiene huecos con un in 
    devolver True o False
    """
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
    '''
    Obtener el numero de filas
    Iterar sobre range(num_filas)
        para cada fila si la victoria_horizontal es true, devuelvo True
        sigo en otro caso

    Si salgo del Bucle devolver false
    '''
    num_filas = len(tablero[0])
    for num_fila in range(num_filas):
        if victoria_horizontal_fila(tablero, num_fila, ficha):
            return True

    return False

def victoria_horizontal_fila(tablero, pos_fila, ficha):
    contador_iguales = 0
    
    for columna in tablero:
        if columna[pos_fila] == ficha:
            contador_iguales += 1
        else:
            contador_iguales = 0

        if contador_iguales == 4:
            return True
    return False

def victoria_diagonal(tablero,ficha):
    
    for x in range(len(tablero) - 3):
        for y in range(len(tablero[x])):
            if tablero[x][y] == ficha and tablero[x][y] != 0:

                if y < 3 and tablero[x+1][y+1] == ficha and tablero[x+2][y+2] == ficha and tablero[x+3][y+3] == ficha:
                    return True

                if y >= 3 and tablero[x+1][y-1] == ficha and tablero[x+2][y-2] == ficha and tablero[x+3][y-3] == ficha:
                    return True
    return False
