class Barco:

    def __init__(self, id_barco, fila, columna, eslora, orientacion):
        '''
        Constructor de un barco
        '''
        self.id_barco = id_barco
        self.fila = fila
        self.columna = columna
        self.eslora = eslora
        self.orientacion = orientacion
        self.vida = eslora
        pass 
    
    def hundido(self):
        '''
        ¿Basta con avisar solo cuando se ha hundido del todo?
        '''
        self.vida -= 1
        return self.vida == 0  # True si el barco se ha hundido