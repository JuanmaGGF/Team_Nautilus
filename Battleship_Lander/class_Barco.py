# Bibliotecas estándar de Python
import random

# Módulos propios
from variables import BARCOS

class Barco:
    
    def __init__(self, nombre, eslora, coordenadas, estado):
        '''
        1) asigna nombre que llega como argumento
        2) asigna tamaño que llega como argumento
        3) asigna coordenada_inicial random
        4) asigna lista_coordenadas llamando a posicionar_barco
        6) genera estado del barco (el numero de celdas del barco con "X", es decir: tocado y/o hundido)
        '''
        self.nombre
        self.eslora
        self.coordenadas
        self.estado 
        pass 

    def inicializar_barcos(self):
        barcos = {}

        for nombre_barco in BARCOS.keys():
            for eslora, cantidad in BARCOS[nombre_barco]:
                posicionar_barco() # type: ignore
                # Crea un diccionario (o lista; aún por definir) de objetos Barco

        return barcos
    
    def tocado_hundido(self):
        '''
        1) recibe coordenada y comprueba si esta en la lista de casillas del barco (lista_coordenadas)
	        1.a) si esta y es "X" imprime "Ya la has dicho" y devuelve False
	        1.b) si no es "X", si está y es "O" disminuye el tamaño de tamaño_tocadas en uno.
	        1.c) Si tamaño_tocadas es = 0 imprime "hundido el barco (nombre)" y devuelve True, si imprime "tocado" y devuelve True.
        2) Si no está en la lista de casillas (lista_coordenadas) devuelve False'''
        pass
    
    def posicionar_barco(self):
        '''
        metodo genera_lista_posiciones
        1) coge la primera casilla y la mete en su lista_coordenadas con el valor "O"
        2) hasta completar su tamaño
	        2.1) comprueba orientacion y define cual es la casilla siguiente
	        2.1) mete siguiente casilla en su lista_coordenadas con el valor "O"
        '''
        pass