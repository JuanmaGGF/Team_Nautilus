# Bibliotecas de terceros
import numpy as np

# Módulos propios
from class_Barco import Barco
from variables import DIMENSION_TABLERO

class Tablero:
    
    '''
    Lo ya definido por Juanma. NO lo copio todo
    '''
    
    def __init__(self, jugador_id):
        '''
        1) asigna el id del jugador al tablero
        2) asigna dimensiones al tablero(es inmutable así que sería una tupla)
        3) inicializa un diccionario de barcos con los barcos que tenemos colocados(recibidos al crear el tablero)
        4) crea barcos_propios = un numpy para barcos
        5) crea barcos_ajenos = un numpy para barcos de la computadora
        6) Inicializa pos brd
        7) Inicializa celdas_tocadas (cantidad de X en barcos_propios)  (más facil contar el total de X hasta que sea 0 y no tener que volver a contarlos otra vez cada vez)
        '''
        self.jugador_id = jugador_id # 'jugador' o 'CPU'
        self.tablero = np.full((DIMENSION_TABLERO, DIMENSION_TABLERO), ' ')
        self.barcos = Barco.inicializar_barcos() # posiciona todos los barcos, de forma aleatoria
        pass
    
    def verificar_espacio(self):
        pass
    
    def colocar_barco(self):
        '''¿o un método de la clase Barco?'''
        pass
    
    def disparar(self):
        pass
    
    def mostrar_tablero(self):
        pass