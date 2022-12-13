import numpy as np

from variables import *
from funciones import *
from clases import *

print("\n ¡¡Bienvenido al maravilloso juego de Hundir la flota!!")
print(sInfo)
print("\n ¡¡VAMOS A JUGAR!! \n")

jugador = Tablero(1, "Jose", lBarcosJugador)
maquina = Tablero(2, "Maquina", lBarcosMaquina)

cResp = input("¿Desea introducir sus barcos de forma automática (A) o de forma manual (M)?").upper()
if cResp == "A":
    jugador.barcos = [[(0,1)], [(2,3)], [(3,1)], [(6,7)], 
                        [(3,7), (3,8)], [(8,4), (8,5)], [(6,4), (6,5)],
                        [(9,8), (9,7), (9,6)], [(7,2), (7,1), (7,0)],
                        [(3,5), (2,5), (1,5), (0,5)]
                    ]
else:
    print("\nIntroduce tus barcos")
    cResp = pintarBarcos(jugador)
    if cResp == False:
        print("\nSe pintaran tus barcos de forma automática.")
        jugador.barcos = [[(0,1)], [(2,3)], [(3,1)], [(6,7)], 
                            [(3,7), (3,8)], [(8,4), (8,5)], [(6,4), (6,5)],
                            [(9,8), (9,7), (9,6)], [(7,2), (7,1), (7,0)],
                            [(3,5), (2,5), (1,5), (0,5)]
                        ]

print("\nTu tablero")
jugador.colocarBarcos(jugador.barcos)

print(jugador.tablero)
#print(maquina.tablero)

numTocadosJugador = 20
numTocadosMaquina = 20

lResp = []

while True:
    print("\n\n *** Es tu turno ***")
    while True:
        lResp = disparar(maquina, jugador.idJugador, numTocadosJugador)
        numTocadosJugador = lResp[1]
        if lResp[0] == "FIN":
            print("\n ¡¡¡¡¡HAS GANADO!!!!!","\n")
            break
        elif lResp[0] == "SALIR":
            print("\n ¡¡HAS ABANDONADO EL JUEGO!!")
            break
        elif lResp[0] == "Agua":
            break

    if lResp[0] == "FIN" or lResp[0] == "SALIR":
        print("\nTu Tablero:\n")
        print(jugador.tablero)

        print("\nTablero Máquina:\n")
        print(maquina.tablero)

        break

    print("\n\n *** Turno de la máquina ***")
    while True:
        lResp = disparar(jugador, maquina.idJugador, numTocadosMaquina)
        numTocadosMaquina = lResp[1]
        if lResp[0] == "FIN":
            print("\n ¡¡HAS PERDIDO!!")
            break
        elif lResp[0] == "Agua":
            break

    if lResp[0] == "FIN":
        print("\nTu Tablero:\n")
        print(jugador.tablero)

        print("\nTablero Máquina:\n")
        print(maquina.tablero)
        break
