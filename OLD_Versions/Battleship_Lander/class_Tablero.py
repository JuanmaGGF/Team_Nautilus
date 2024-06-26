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


    def mostrar_tableros(self, tablero_oponente, *, ocultar_barcos = True):
        '''
        Muestra los dos tableros en paralelo.
        Si "ocultar_barcos = True" esconde los barcos del "tablero_oponente". Es decir cambiar 'O' (barco) por ' ' (agua)
        '''
        jugador_oponente = tablero_oponente.jugador_id
        
        if ocultar_barcos:
            tablero_oponente = np.where(tablero_oponente.tablero == 'O', ' ', tablero_oponente.tablero)
        else:
            tablero_oponente = tablero_oponente.tablero
        
        #print(self.jugador_id, ':', '\t'*5, jugador_oponente, ':')   
        print(f'{self.jugador_id}:{'\t'*5} {jugador_oponente}:\n')            
         
        for fila in range(DIMENSION_TABLERO):
            print(self.tablero[fila], '\t', tablero_oponente[fila])
     
     
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
    
    
    def disparar(self, tablero_oponente, coordenadas):
        '''
        Probablemente llamará a "_recibir disparo" y a _tocado_hundido
        '''
        pass
    
    def _recibir_disparo(self, coordenadas):
        '''
        ### Método privado ###
        '''
        pass

    def _tocado_hundido(self):
        '''
        ### Método privado ###
        '''
                    