import numpy as np

from class_Barco import Barco
from variables import BARCOS, DIMENSION_TABLERO

class Tablero:
        
    def __init__(self, jugador_id):
        '''
        1) Asigna el id del jugador al tablero
        2) Asigna dimensiones al tablero (inmutable) y lo inicia con agua (' ')
        3) Inicializa un diccionario de barcos para el tablero
        4) Posiciona los barcos en el tablero llamando al método Tablero.inicializar_barcos()
        '''
        self.jugador_id = jugador_id
        self.tablero = np.full((DIMENSION_TABLERO, DIMENSION_TABLERO), ' ')
        self.barcos = {}
        self.inicializar_barcos() # posiciona todos los barcos de forma aleatoria
    
    def inicializar_barcos(self):
        '''
        Inicializa y posiciona los barcos definidos en la variable global "BARCOS"
        '''
        for (nombre, (eslora, cantidad)) in BARCOS.items():
            for num_barco in range(cantidad):
                colocado = False
                while not colocado:
                    fila = np.random.randint(0, DIMENSION_TABLERO)
                    columna = np.random.randint(0, DIMENSION_TABLERO)
                    orientacion = np.random.choice(['H', 'V'])
                    if self._posicion_valida(fila, columna, eslora, orientacion):
                        self._ubicar_barco(fila, columna, eslora, orientacion)
                        id_barco = f'{nombre}_{str(num_barco)}'
                        self.barcos[id_barco] = Barco(id_barco, fila, columna, eslora, orientacion)
                        colocado = True
                            
    def _ubicar_barco(self, fila, columna, eslora, orientacion):
        '''
        ### Método privado ###
        Ubica en el tablero la posición de un barco: pinta "O" en las posiciones que ocupe en barco.
        '''
        if orientacion == 'H':
            for i in range(eslora):
                self.tablero[fila, columna + i] = 'O'
        else:
            for i in range(eslora):
                self.tablero[fila + i, columna] = 'O'
    
    def _posicion_valida(self, fila, columna, eslora, orientacion):
        '''
        ### Método privado ###
        Comprueba si el barco se puede ubicar en el tablero.
            --> True  : El barco se puede ubicar en el tablero.
            --> False : El barco no se puede ubicar en el tablero (excede las dimensiones del 
                        tablero o se solapa con otro barco)
        '''
        if orientacion == 'H':
            if columna + eslora > DIMENSION_TABLERO:
                return False
            for i in range(eslora):
                if self.tablero[fila, columna + i] != ' ':
                    return False
        else:
            if fila + eslora > DIMENSION_TABLERO:
                return False
            for i in range(eslora):
                if self.tablero[fila + i, columna] != ' ':
                    return False
        return True    
    
    def disparar(self):
        '''
        Si acierta llamara al método Barco.recibir_impacto
        '''
        pass
    
    def mostrar_tablero(self, jugador_id):
        '''
        ¿Un print bastará?
        Puede tener un argumento de entrada para en función de quién este jugando mostrar los barcos u ocultarlos
        jugador_id podría ser una variable booleana según sea humano o máquina el jugador
        '''
        pass
