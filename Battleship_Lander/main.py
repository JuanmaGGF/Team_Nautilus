# Bibliotecas estándar de Python
import random

# Bibliotecas de terceros
import numpy as np      # No creo que haga falta importarlo aquí

# Módulos propios
from class_Tablero import Tablero

def juego():
    
    print('Bienvenido a Hundir la Flota')
    print('Instrucciones del juego:') # Instrucciones simples del juego
    tablero_jugador = Tablero(jugador_id = 'Jugador')
    tablero_maquina = Tablero(jugador_id = 'Maquina')

    juego_terminado = False
    turno_jugador = True

    while not juego_terminado:
        if turno_jugador:
            '''
            1 - Mostrar tableros
            2 - Pedir coordenadas
                2.1 Con comandos especiales salir de la partida o mostrar menú del juego
            3 - while ¿Tocado o hundido?
                3.1 Volver a pedir coordenadas
            '''
        else: # turno de la máquina
            '''
            Código similar al del 'Jugador' pero son métodos random
                - Nota: No puede disparar a casillas que ya ha disparado
            '''

# El código se ejecuta solo cuando el script se ejecuta directamente, y no cuando se importa como un módulo en otro script
if __name__ == "__main__":
    juego()
