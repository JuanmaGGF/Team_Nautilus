import numpy as np
import barco

class Tablero:

    def __init__(self,jugador,dimensiones,barcos):
        # Creamos el constructor del tablero con el nombre del jugador y las dimensiones (lista de 2 dimensiones X e Y) del tablero
        # jugador sera un string, dimensiones un valor entero y barcos una lista de objetos barcos
        self.jugador = jugador #Asigno el nombre del jugador
        # A continuacion metemos la lista de barcos
        self.lista_barcos = barcos # guardo la lista de barcos pasada
        # Preparamos el tablero del jugador inicializandoo a sin barcos
        self.barcos_propios = np.full((dimensiones,dimensiones)," ")
        # Preparamos el tablero para ir viendo los disparos en el del enemigo
        self.barcos_ajenos = np.full((dimensiones,dimensiones)," ")
        # Guardamos el numero de celdas tocadas que cuando se reduzca a 0 significará que el otro jugador ha ganado la partida.
        self.celdas_tocadas = 20 # este valor esta puesto a voleo, luego será el de la cantidad de celdas que ocupen los barcos
        # Guardamos las dimensiones del tablero para comprobar si cae fuera un barco o disparo
        self.dimensiones = [dimensiones,dimensiones]
        # Colocamos los barcos
        self.inicializa()
    
    def muestra_tableros(self):
        #Este metodo muestra los dos tableros en paralelo en vez de uno debajo de otro para mayor comodidad visual
        print("\n") # hacemos un espacio de dos saltos de linea
        print(self.jugador,"\t\t\t\t\t\t","Enemigo") # Imprimos encima de cada tablero quien de quien es
        for fila in range(self.dimensiones[1]): # Imprimimos fila por fila
            print(self.barcos_propios[fila],"\t",self.barcos_ajenos[fila]) # Para cada fila imprimo el del jugador y el de su enemigo

    def esta_fuera(self,nombre,coordenadas):
        # Este método comprueba si la coordenada está fuera del panel
        for coordenada in coordenadas: #Coge cada coordenada del barco
            if (coordenada[0] > self.dimensiones[0]) or (coordenada[1] > self.dimensiones[1]): #Comprueba si la coordenadaX > dimensionX y cooerdenadaY > dimensionY            
                print("- ", nombre, "esta fuera de los limites de juego") 
                return True
        return False
    
    def interfiere(self,nombre,posiciones):
        # Este metodo comprueba si al intntar colocar algún barco interfiere con otro
        for barco in self.lista_barcos: # Cojo cada barco y sus coordenadas en el diccionario
            coordenadas_existentes = barco.get_coordenadas()
            for coordenada in posiciones: # Cojo cada coordenada del barco completo
                for coordenada_existente in coordenadas_existentes:
                    if (nombre!=barco.get_nombre()) and (coordenada[0]==coordenada_existente[0]) and (coordenada[1]==coordenada_existente[1]) : # Miro si no es el mismo barco que estoy comprobando y la coordenada esta dentro de las del barco
                        print("- ", nombre, "interfiere con", barco.get_nombre())
                        return True
        return False
    
    def coloca_barco(self,coordenadas):
        # Este método coloca un barco completo
        for coordenada in coordenadas:
            self.barcos_propios[coordenada[0],coordenada[1]] = "O" # Coge cada barco y lo mete en el np.array de barcos propios
  
    def inicializa(self):
        # Inicializa se encarga de colocar los barcos en el tablero y ver si caben bien
        print("\n") # Hacemos un espaciovpara dejar visibilidad
        # Primero comprueba que no tiene problemas, ya que si no habrá que corregirlo
        problemas = False
        for barco in self.lista_barcos: # Coge cada barco de la lista
            if self.esta_fuera(barco.get_nombre(),barco.get_coordenadas()) or self.interfiere(barco.get_nombre(),barco.get_coordenadas()): # Si está fuera o interfiere con otro barco no los coloco
                problemas = True
        if not problemas:
            for barco in self.lista_barcos: # Coge cada barco de la lista
                self.coloca_barco(barco.get_coordenadas()) # Coloca el barco una vez comprobado lo anterior
            self.muestra_tableros() # Imprime los tableros
        else:
            print("Los barcos no pudieron colocarse")
            print("\n")
    

    def comprueba_estado_juego(self):
        # Esta celda mira a ver si el juego ha acabado o no
        if self.celdas_tocadas == 0: # Cuando todas las celdas de los barcos están tocadas ya está acabado
            print("Juego finalizado", self.jugador, "pierde")
    
    #EL METODO recibir_disparo ANTERIOR ESTA HECHO CON DICCIONARIO DE BARCOS PARA PROBAR, ESTE SERA EL DEFINITIVO CUANDO ESTE LA CLASE BARCOS
    def recibir_disparo(self,coord):
        # Este metodo está para que un jugador pueda llamar al tablero y hacer un disparo
        if self.esta_fuera("Disparo",[coord]):
            print("fuera de rango") # Si está fuera de las dimensiones lo indica
        else:
            for barco in self.lista_barcos: # Coge la lista de barcos
                if barco.tocado_hundido(coord):     # Llama al metodo de barco para ver si esta tocado o hundido, Tengo que pasar una lista de coord
                    self.celdas_tocadas -= 1        # Si es así reduce el numero de celdas a tocar
                    self.comprueba_estado_juego     # Luego comprueba el estado del juego
                    return "X"                      # Si le ha dado retorna "X"               
            print("Agua!")
            return "-"                      # Si no le ha dado retorna "-" 
    


# A PARTIR DE AQUI HAGO UNA COMPROBACION DE SI FUNCIONA. OJO QUE USO SIEMPRE LA MISMA LISTA DE BARCOS COLOCADOS (LA MIA)
# HABRA QUE CREAR DOS JUGADORES Y COMPROBAR CON LA DEL OTRO

# Aquí se genera la lista de barcos a pasar para crear el tablero (ESTO IRIA EN OTRA CLASE como MAIN o JUGADOR)
lista_barcos = []
barco1 = barco.Barco("Titanic",[[1,3],[1,4],[1,5]])
barco2 = barco.Barco("Riviera",[[2,1],[3,1],[4,1]])
barco3 = barco.Barco("Queen Elizabeth",[[6,1],[6,2]])
barco4 = barco.Barco("Elcano",[[8,1],[8,2],[8,3],[8,4]])
lista_barcos.append(barco1)
lista_barcos.append(barco2)
lista_barcos.append(barco3)
lista_barcos.append(barco4)
tablero = Tablero("Juanma",10,lista_barcos)

# Aqui se realizan los disparos, (ESTO IRIA EN OTRA CLASE como MAIN o JUGADOR.
seguimos = True                                               #variable que controla si seguimos
while seguimos:
    x = int(input("Coordenada X?"))
    y = int(input("Coordenada Y?"))
    tablero.barcos_ajenos[x,y] = tablero.recibir_disparo([x,y])
    tablero.muestra_tableros()
    entrada = input("Otro disparo? (\"F\" para terminar, cualquier tecla para seguir").upper()
    if entrada == "F":
        seguimos = False
