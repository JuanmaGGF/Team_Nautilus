import numpy as np

from class_Tablero import Tablero
from funciones import solicitar_coordenadas

def juego():
    '''
    Función principal del juego
    '''
    
    print('\n ~~~~ Bienvenidx a Hundir la Flota ~~~~ \n')
    print('Escriba "exit" en cualquier momento para terminar el juego\n') # ¿Añadir instrucciones simples del juego?
    
    tablero_jugador = Tablero(jugador_id = 'Jugador') 
    tablero_maquina = Tablero(jugador_id = 'Máquina')

    juego_terminado = False
    turno_jugador = True
    
    # print(tablero_jugador)
    # print(type(tablero_jugador.tablero))
    
    while not juego_terminado:
        if turno_jugador:
            tablero_jugador.mostrar_tableros(tablero_maquina, ocultar_barcos = False) # ocultar_barcos = False de momento para ver como va la partida
            coordenadas = solicitar_coordenadas(),
            tablero_maquina.recibir_disparo(coordenadas)
            break


if __name__ == "__main__":
    juego()  



# PSEUDO-CÓDIGO DE FUNCIONAMIENTO
# Resume las funciones principales del programa
'''
def juego():
    
    1. Dar bienvenida e instrucciones del juego
    
    2. Crear tablero para jugador y máquina

    juego_terminado = False
    turno_jugador = True

    while not juego_terminado:
        if turno_jugador:
            
            1 - Mostrar tableros
            2 - Pedir coordenadas
                2.1 Con comandos especiales salir de la partida o mostrar menú del juego
            3 - while ¿Tocado o hundido?
                3.1 Volver a pedir coordenadas
            
        else: # turno de la máquina
            
            Código similar al del 'Jugador' pero son métodos random
                - NOTA: No puede disparar a casillas que ya ha disparado
'''