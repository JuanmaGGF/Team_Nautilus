class Barco:

    ### puede ser interesante que en vez de guardar solo la fila y columna inicial
    ### guarde todo el vector que ocupa. Así sabremos si hay que restarle una 
    def __init__(self, id_barco, fila, columna, eslora, orientacion):
        '''
        Constructor de un barco.
        '''
        self.id_barco = id_barco
        self.fila = fila
        self.columna = columna
        self.eslora = eslora
        self.orientacion = orientacion
        
        self.vida = eslora 
    
    def hundido(self):
        '''
        ¿Basta con avisar solo cuando se ha hundido?
        '''
        self.vida -= 1
        return self.vida == 0  # True si el barco se ha hundido