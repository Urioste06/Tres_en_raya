
from colorama import init, Fore, Style
init(autoreset=True)

#Instrucciones del juego
print(Fore.YELLOW + '''INSTUCCIONES\n  Buenas este juego consite en conseguir mediante turnos en el tablero, una línea.
     El juego pedirá que introduzcas el nombre del jugador 1 y elijas el símbolo con el que quieres jugar,
     luego perirá el nombre del jugador 2 y le dejará el símbolo que no haya elegido el jugador 1.
     El juego va por coordenadas, del 0 al 2 tanto en filas que es lo primero que te pedirá y luego por 
     columnas. El juego termina cuando alguno de los dos jugadores haya conseguido los que se denomina tres
     en raya, alinear tres símbolos seguidos en línea tanto horizontal como vertical o en las diagonales.
     También terminará cuando ninguno de los dos jugadores haya conseguido tal proposito y no haya más huecos
     por ocupar, eso indicará que hay EMPATE ''')

import colored

def crear_tablero():
    
    # Función que crea un tablero vacío para jugar al tres en raya.
    
    tablero = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    return tablero

def imprimir_tablero(tablero):
    
    #Función que imprime el tablero actual del juego.
    # Se utiliza coloreama con Fore.GREEN para dar color al símbolo introducido en este caso la 'X' verde y la 'O' roja. 
    # Se colocan todas las posibilidades que hay por cada fila. Según David no hay que poner tantos comentarios, pero si
    # no los pongo no me entero. Voy a explicar la primera fila, dibulo el tablero (que se podría mejorar), y las llaves,
    # llevan los valores X ó O que vayamos introduciendo. Le doy formato a todos de color verde con Fore.GREEN si son igual
    # a 'X' y si es otro se pone en rojo con Fore.RED.
    
    print('   0   1   2')
    print('0  {} | {} | {}'.format(Fore.GREEN + tablero[0][0] + Style.RESET_ALL if tablero[0][0] == 'X' else Fore.RED + tablero[0][0] + Style.RESET_ALL,
                                  Fore.GREEN + tablero[0][1] + Style.RESET_ALL if tablero[0][1] == 'X' else Fore.RED + tablero[0][1] + Style.RESET_ALL,
                                  Fore.GREEN + tablero[0][2] + Style.RESET_ALL if tablero[0][2] == 'X' else Fore.RED + tablero[0][2] + Style.RESET_ALL))
    print('  ---+---+---')
    print('1  {} | {} | {}'.format(Fore.GREEN + tablero[1][0] + Style.RESET_ALL if tablero[1][0] == 'X' else Fore.RED + tablero[1][0] + Style.RESET_ALL,
                                  Fore.GREEN + tablero[1][1] + Style.RESET_ALL if tablero[1][1] == 'X' else Fore.RED + tablero[1][1] + Style.RESET_ALL,
                                  Fore.GREEN + tablero[1][2] + Style.RESET_ALL if tablero[1][2] == 'X' else Fore.RED + tablero[1][2] + Style.RESET_ALL))
    print('  ---+---+---')
    print('2  {} | {} | {}'.format(Fore.GREEN + tablero[2][0] + Style.RESET_ALL if tablero[2][0] == 'X' else Fore.RED + tablero[2][0] + Style.RESET_ALL,
                                  Fore.GREEN + tablero[2][1] + Style.RESET_ALL if tablero[2][1] == 'X' else Fore.RED + tablero[2][1] + Style.RESET_ALL,
                                  Fore.GREEN + tablero[2][2] + Style.RESET_ALL if tablero[2][2] == 'X' else Fore.RED + tablero[2][2] + Style.RESET_ALL))

def obtener_jugada(jugador, simbolo, tablero):
    
    # Función que pide al jugador las coordenadas para hacer una jugada válida en el tablero.
    
    #print('Turno del jugador', jugador)
    #fila = int(input('Escribe ta fila donde desea colocar {}: '.format(simbolo)))
    #columna = int(input('Escribe ta columna donde desea colocar {}: '.format(simbolo)))
    #return (fila, columna)
    print('Turno del jugador', jugador)
    while True:
        try:
            fila = int(input('Escribe ta fila donde desea colocar {}: '.format(simbolo)))
            columna = int(input('Escribe ta columna donde desea colocar {}: '.format(simbolo)))
            if fila < 0 or fila > 2 or columna < 0 or columna > 2:
                print('Las filas y columnas deben ser números entre 0 y 2.')
            elif tablero[fila][columna] != ' ':
                print('La casilla ya está ocupada. Intente de nuevo.')
            else:
                return (fila, columna)
        except ValueError:
            print('Escribe talores numéricos para fila y columna.')
def actualizar_tablero(tablero, fila, columna, simbolo):
    
    # Función que actualiza el tablero con la jugada realizada.
    
    tablero[fila][columna] = simbolo

def verificar_ganador(tablero, simbolo):
    
    # Función que verifica si el jugador con el símbolo elegido ha ganado.
    
    # Verificar filas
    for fila in range(3):
        if tablero[fila][0] == simbolo and tablero[fila][1] == simbolo and tablero[fila][2] == simbolo:
            return True

    # Verificar columnas
    for columna in range(3):
        if tablero[0][columna] == simbolo and tablero[1][columna] == simbolo and tablero[2][columna] == simbolo:
            return True

    # Verificar diagonales
    if tablero[0][0] == simbolo and tablero[1][1] == simbolo and tablero[2][2] == simbolo:
        return True
    if tablero[0][2] == simbolo and tablero[1][1] == simbolo and tablero[2][0] == simbolo:
        return True

    # Si no hay ganador, devolver False
    return False

def verificar_empate(tablero):
    
    # Función que verifica si hay empate en el juego.
    
    for fila in range(3):
        for columna in range(3):
            if tablero[fila][columna] == ' ':
                return False
    return True

def jugar_tres_en_raya():
    
    #Función principal del juego.
    
    print(Fore.CYAN + '¡Bienvenido al juego del Tres en Raya!')

    # Pedir nombres de los jugadores y qué símbolo quieren
    
    nombre_jugador1 = input('Jugador 1, Escribe tu nombre: ')
    simbolo_jugador1 = input('{} ¿Quieres jugar con X o con O?: '.format(nombre_jugador1)).upper()
    while simbolo_jugador1 != 'X' and simbolo_jugador1 != 'O':
        simbolo_jugador1 = input('Escribe una opción válida (X/O): ').upper()

    
    nombre_jugador2 = input('Jugador 2, Escribe tu nombre: ')
    if simbolo_jugador1 == 'X':
        simbolo_jugador2 = 'O'
    else:
        simbolo_jugador2 = 'X'

    # Iniciar el juego
    tablero = crear_tablero()
    imprimir_tablero(tablero)

    # Jugar hasta que haya ganador o empate
    while True:
        # Turno del jugador 1
        jugada = obtener_jugada(nombre_jugador1, simbolo_jugador1, tablero)
        while tablero[jugada[0]][jugada[1]] != ' ':
            print('La casilla ya está ocupada. Intente de nuevo.')
            jugada = obtener_jugada(nombre_jugador1, simbolo_jugador1, tablero)
        actualizar_tablero(tablero, jugada[0], jugada[1], simbolo_jugador1)
        imprimir_tablero(tablero)
        if verificar_ganador(tablero, simbolo_jugador1):
            print('¡Felicidades, {} ha ganado!'.format(nombre_jugador1))
            break
        if verificar_empate(tablero):
            print('¡Empate!')
            break

        # Turno del jugador 2
        jugada = obtener_jugada(nombre_jugador2, simbolo_jugador2, tablero)
        while tablero[jugada[0]][jugada[1]] != ' ':
            print('La casilla ya está ocupada. Intente de nuevo.')
            jugada = obtener_jugada(nombre_jugador2, simbolo_jugador2, tablero)
        actualizar_tablero(tablero, jugada[0], jugada[1], simbolo_jugador2)
        imprimir_tablero(tablero)
        if verificar_ganador(tablero, simbolo_jugador2):
            print('¡Felicidades, {} ha ganado!'.format(nombre_jugador2))
            break
        if verificar_empate(tablero):
            print('¡Empate!')
            break
jugar_tres_en_raya()
