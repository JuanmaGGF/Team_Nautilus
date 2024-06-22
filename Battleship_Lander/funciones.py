import sys

# Se puede mejorar haciendo control de entrada y checkear que esta sea válida
def solicitar_coordenadas(): 
    '''
    Solicita y genera coordenadas en forma de tupla (x, y).
    IMPORTANTE : Si el usuario escribe "exit" se interrumpe la ejecución de Python.
    '''
    coordenadas_input = input('\nIngrese las coordenadas en formato x,y:')
    if coordenadas_input == 'exit':
        sys.exit()
    coordenada_x, coordenada_y = coordenadas_input.split(',')
    return (int(coordenada_x), int(coordenada_y))