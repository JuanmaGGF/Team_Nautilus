import sys

def solicitar_coordenadas(): # se puede hacer control de entrada y checkear que esta sea válida
    '''
    Solicita y genera una coordenadas en forma de tupla (x, y).
    Si el usuario escribe "exit" se para la ejecución de Python.
    '''
    while True:
        coordenadas_input = input('\nIngrese las coordenadas en formato x,y:')
        if coordenadas_input == 'exit':
            sys.exit()
        coordenada_x, coordenada_y = coordenadas_input.split(',')
        coordenadas = [int(coordenada_x),int(coordenada_y)]
        if (coordenadas[0] >= 0 and coordenadas[0] < 10) and  (coordenadas[1] >= 0 and coordenadas[1] < 10):
            return coordenadas