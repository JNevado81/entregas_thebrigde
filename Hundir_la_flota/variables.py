sInfo = "\n Dispondrás de 10 barcos de distintas dimensiones: " \
        "\n     4 barcos de 1 posición de eslora \n     3 barcos de 2 posiciones de eslora \n     2 barcos de 3 posiciones de eslora \n     1 barco de 4 posiciones de eslora" \
        "\n\n Los barcos se van a colocar de forma automática o de forma manual, según elija." \
        "\n\n Si quieres salir del juego tienes que escribir 9999 en la consola." \

lBarcosJugador = []

lBarcosMaquina = [[(0,1)], [(2,3)], [(3,1)], [(6,7)], 
                    [(3,7), (3,8)], [(8,4), (8,5)], [(6,4), (6,5)],
                    [(9,8), (9,7), (9,6)], [(7,2), (7,1), (7,0)],
                    [(3,5), (2,5), (1,5), (0,5)]
                ]

"""
barcos_ = {
        "barco_1_1": (1, [(0,1)], 0),
        "barco_1_2": (1, [(2,3)], 0),
        "barco_1_3": (1, [(3,1)], 0),
        "barco_1_4": (1, [(6,7)], 0),
        "barco_2_1": (2, [(3,7), (3,8)], 0),
        "barco_2_2": (2, [(8,4), (8,5)], 0),
        "barco_2_3": (2, [(6,4), (6,5)], 0),
        "barco_3_1": (3, [(9,8), (9,7), (9,6)], 0),
        "barco_3_2": (3, [(7,2), (7,1), (7,0)], 0),
        "barco_4_1": (4, [(3,5), (2,5), (1,5), (0,5)], 0),
        }
"""