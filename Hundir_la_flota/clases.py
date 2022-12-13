import numpy as np

# Implementar la clase "Tablero"
class Tablero():
    '''
    Clase Tablero
    Parametros comunes:
        tablero (np.array)
        tableroDisparos (np.array)
    '''
    # Atributos de la clase
    tablero = np.full(10, 10)
    tableroDisparos = np.full(10, 10)

    # Constructor
    def __init__(self, idJugador:int, nombre:str, barcos:list, dimensiones:int=10):
        '''
        Documentacion de la inicialización
        Parametros propios:
            idJugador (int)
            nombre (str)
            barcos (list)
            dimensiones (int)
        '''
        self.idJugador = idJugador
        self.nombre = nombre
        self.barcos = barcos
        self.dimensiones = dimensiones
        self.inicializarTablero(dimensiones)
        self.colocarBarcos(self.barcos)

    # Método 
    def inicializarTablero(self, dimensiones):
        '''
        Método 
        '''
        self.dimensiones = dimensiones
        self.tablero = np.full((self.dimensiones, self.dimensiones), " ")

    # Método 
    def colocarBarcoManual(self, barco:list):
        '''
        Método 
        '''
        for coordenada in barco:
            self.tablero[coordenada] = "O"

        self.barcos.append(barco)

    # Método 
    def colocarBarco(self, barco:list):
        '''
        Método 
        '''
        for coordenada in barco:
            self.tablero[coordenada] = "O"

    # Método 
    def colocarBarcos(self, listaBarcos:list):
        '''
        Método 
        '''
        for barco in listaBarcos:
            self.colocarBarco(barco)

    # Método 
    def disparar(self, casilla:list):
        '''
        Método 
        '''
        if self.tablero[casilla] == "O":
            self.tablero[casilla] = "X"
            return "Tocado"
        elif self.tablero[casilla] == " " or self.tablero[casilla] == "-":
            self.tablero[casilla] = "-"
            return "Agua"
