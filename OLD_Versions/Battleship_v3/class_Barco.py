class Barco:

    def __init__(self, id_barco, fila, columna, eslora, orientacion):
        '''
        Constructor de un barco.
        '''
        self.id_barco = id_barco
        self.fila = fila
        self.columna = columna
        self.eslora = eslora
        self.orientacion = orientacion
        self.tocadas = []                   # Guardo las celdas tocadas para saber si está hundido o no
        self.vida = eslora

    
    def hundido(self):
        '''
        ¿Basta con avisar solo cuando se ha hundido del todo?
        '''
        self.vida -= 1
        return self.vida == 0  # True si el barco se ha hundido. 

    # Checkar este metodo
    # self.tocadas podría ser una lista de tuplas
    def repetida(self, coordenadas):  
        '''
        Este metodo dice si la tirada es repetida.
        '''                                         
        for tocada in self.tocadas:
            if tocada[0] == coordenadas[0] and tocada[1] == coordenadas[1]:
                print("Ya se había disparado aquí.")
                return True
            return False

    # ¿esto no retorna nada? no necesitas las posiciones del barco o no las usas para nada?
    def tocado(self,coordenadas):
        '''
        Vamos a mirar si ha tocado al barco.
        '''
        repetida = self.repetida(coordenadas)                   # Compruebo que no esté repetida la tirada
        lista_posiciones = []                                   # Primero generamos una lista para saber qué posiciones tiene el barco
        if self.orientacion == 'H':
            posicionX = self.fila
            for zona in range(self.eslora):
                posicionY = zona+self.columna
                lista_posiciones.append([posicionX,posicionY])
        elif self.orientacion == 'V':           
            posicionY = self.columna
            for zona in range(self.eslora):
                posicionX = zona+self.fila
                lista_posiciones.append([posicionX,posicionY])

        for posicion in lista_posiciones:                                           # Ahora comprobamos si da en alguna
            if (coordenadas[0]==posicion[0]) and (coordenadas[1]==posicion[1]):     # Si la tirada ha tocado alguna posicion la guardo en la lista de tocadas              
                self.tocadas.append([coordenadas[0],coordenadas[1]])                
                if (not repetida):                                                  # Si la tirada no está repetida miro a ver si está hundido
                    if self.hundido():
                        print("Hundido",self.id_barco,"!!")
                        print()
                    else:                                                           # Si no está hundido y no está repetida imprimo "Tocado"
                        if not repetida:
                            print("Tocado !!")
                            print()
                    return True                                                     # Devuelvo True si ha sido tirada con éxito y False si no
                else:
                    return False
        return False