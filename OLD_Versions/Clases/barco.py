import numpy as np

class Barco:
#Genera la clase Barco
    
    def __init__(self,nombre,coordenadas):
    #Constructor de Barco
        self.nombre = nombre                            #Asigna el nombre
        self.coordenadas = np.array(coordenadas)        #Asigno las coordenadas del barco
        self.tocadas = np.full(len(coordenadas),"O")    #Creo un array de celdas tocadas para saber si hundo el barco

    def get_nombre(self):
        return self.nombre                              #Devuelve el nombre
    
    def get_coordenadas(self):
        return self.coordenadas                         #Devuelve la lista de coordenadas
    
    def tocado_hundido(self,coord):
    # Este metodo nos dice si tocamos o hundimos el barco y devuelve "X" o "-" si le damos o es agua
        coord_arr = np.array(coord)                             #Creamos un np.array con las coordenadas del disparo
        tocado = False                                          #Establecemos todado a Falso
        for coordenada in self.get_coordenadas():               #Comprobamos que el disparo cae en el barco para cada casilla que ocupa                 
            if (coord_arr[0]==coordenada[0]) and (coord_arr[1]==coordenada[1]):       
                tocado = True
        if tocado:                                              
            for i,coord in enumerate(self.get_coordenadas()):   #Si está tocado vemos si ya lo estaba
                if (coord == coord_arr).all():                  
                    if (self.tocadas[i] == "X"):                #Si las coordenadas del disparo ya estaban (tenía la casilla "X")
                        print("Coordenada repetida")            #Imprimo "Repetida"
                    else:
                        self.tocadas[i] = "X"                   #Si no, marco con X
                        if (np.all(self.tocadas == "X")):                   #Si ademas todo el array "tocadas" tiene "X" está hundido
                            print("Barco",self.get_nombre(),"hundido!!!!")  #Devuelvo hundido
                        else:
                            print("Tocado!!")                               #Imprimo "Tocado"                              
            return True                                         #Devuelvo Verdad
        else:                                   #Si no devuelvo "Agua"
            return False                                        #Y devuelvo False

