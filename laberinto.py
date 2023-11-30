
import os


def limpiar_terminal():
    # Función para que se borre el terminal con cada imput
    os.system('cls' if os.name == 'nt' else 'clear')

laberinto = [
    [' ', 'X', 'X', 'X', 'X'], 
    [' ', 'X', ' ', ' ', ' '],
    [' ', 'X', ' ', 'X', ' '], 
    [' ', ' ', ' ', 'X', ' '], 
    ['X', 'X', 'X', 'X', 'S']
]
# Diccionario para traducir los imputs 
traduccionmovimientos = {"b":"abajo", "s": "subir", "d":"derecha", "i": "izquierda"}
movimientos = []

muros = set(((0, 1), (0, 2), (0, 3), (0, 4), (1, 1), (2, 1), (2, 3), (3, 3), (4, 0), (4, 1), (4, 2), (4, 3)))

posicion_actual = (0, 0)
# Metodo para imprimir el laberinto
def imprimir_laberinto(posicion_jugador):
    for i, fila in enumerate(laberinto):
        for j, columna in enumerate(fila):
            if (i, j) == posicion_jugador:
                print('P', end=' ')
            elif (i, j) in muros:
                print('X', end=' ')
            else:
                print(columna, end=' ')
        print()
# Metodo para moverse por el laberinto
def moverse(posicion_jugador, direccion):
    i, j = posicion_jugador
    nueva_posicion = ()

    if direccion == 's' and i > 0 and (i - 1, j) not in muros:
        nueva_posicion = (i - 1, j)
    elif direccion == 'b' and i < len(laberinto) - 1 and (i + 1, j) not in muros:
        nueva_posicion = (i + 1, j)
    elif direccion == 'i' and j > 0 and (i, j - 1) not in muros:
        nueva_posicion = (i, j - 1)
    elif direccion == 'd' and j < len(laberinto[0]) - 1 and (i, j + 1) not in muros:
        nueva_posicion = (i, j + 1)

    return nueva_posicion
# Establece cuando termina el laberinto y los movimientos que has hecho
while True:
    limpiar_terminal()
    imprimir_laberinto(posicion_actual)
    if laberinto[posicion_actual[0]][posicion_actual[1]] == 'S':
        print('¡Felicidades! Has llegado a la salida.')
        print("tus movimientos han sido:", ",".join(movimientos))
        break

    direccion = input("Ingrese la dirección (s-subir, b-bajar, i-izquierda, d-derecha): ").lower()
    
# añade a la lista "movimientos" las direcciones y establece cual es la nueva posicion
    if direccion in ["s", "b", "d", "a"]:
        
        movimientos.append(traduccionmovimientos[direccion])
        nueva_posicion = moverse(posicion_actual, direccion)

        if nueva_posicion:
            posicion_actual = nueva_posicion
        else:
            print("Movimiento no válido. Inténtalo de nuevo.")
    else:
        print("Entrada no válida. Por favor, ingrese s, b, i o d.")
