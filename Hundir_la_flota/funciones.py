import random
from variables import *
from clases import *

#Pendiente 
# --> barcos aleatorios respetando los espacios.
# --> implementar atributo tableroDisparos para saber los disparos que hago aunque ya lo tiene registrado el tablero contrario.
# --> implementar barcos_ para tener todo más compacto y tener controlado los hundidos y tocados.

def pintarBarcos(tablero):
    nCont = 0

    while nCont < 10:
        print(tablero.tablero)

        nFil = int(input("\n Dime la fila:"))
        if nFil == 9999:
            return False

        nCol = int(input("\n Dime la columna:"))
        if nCol == 9999:
            return False

        tablero.colocarBarcoManual([(nFil, nCol)])
        print("\n\n Coordenadas:",tablero.barcos,"\n")

        nCont = nCont + 1
    return True


def disparar(tablero, idJugador:int, numTocados:int):
    lResp = []

    if idJugador == 1: #Judador físico
        nFil = int(input("\n Dime la fila:"))
        if nFil == 9999:
            lResp = ["SALIR", numTocados]
            return lResp

        nCol = int(input("\n Dime la columna:"))
        if nCol == 9999:
            lResp = ["SALIR", numTocados]
            return lResp

    else: #Máquina
        nFil = random.randint(0, 9)
        nCol = random.randint(0, 9)

    sResp = tablero.disparar((nFil, nCol))

    if sResp == "Agua":
        print("\n ¡¡AGUA!!",(nFil, nCol),"\n")

        if idJugador == 2: #Máquina
            print(tablero.tablero)

        lResp = ["Agua", numTocados]
        return lResp

    elif sResp == "Tocado":
        print("\n ¡¡TOCADO!!",(nFil, nCol),"\n")

        if idJugador == 2: #Máquina
            print(tablero.tablero)

        numTocados = numTocados - 1

        if numTocados == 0:
            lResp = ["FIN", numTocados]
            return lResp
        else:
            lResp = ["Tocado", numTocados]
            return lResp
