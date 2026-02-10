"""
CONSTANTS.PY
La única fuente de la verdad. Configuración global del juego Onitama.
"""

# tablero
ROWS = 5
COLS = 5
BOARD_SIZE = 5  #variable por si acaso

# jugadores 
PLAYER_RED = 'RED'
PLAYER_BLUE = 'BLUE'

#piezas
# M maestro , s estudiante
PIECE_MASTER = 'M'
PIECE_STUDENT = 'S'

# configuracion grafica

class Colors:
    RESET = '\033[0m'
    RED_TXT = '\033[91m'
    BLUE_TXT = '\033[94m'
    GREEN_TXT = '\033[92m'  # mov
    YELLOW_TXT = '\033[93m' # advertencias
    BOLD = '\033[1m'

# simbolos visuales
SYMBOLS = {
    (PLAYER_RED, PIECE_MASTER): 'R_M',   # como ♔
    (PLAYER_RED, PIECE_STUDENT): 'r_s',  # ♙
    (PLAYER_BLUE, PIECE_MASTER): 'B_M',
    (PLAYER_BLUE, PIECE_STUDENT): 'b_s',
    'EMPTY': '.'
}

# posicion inicial
START_POSITIONS = {
    PLAYER_RED: [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)], # parte de arribaa
    PLAYER_BLUE: [(4, 0), (4, 1), (4, 2), (4, 3), (4, 4)] # "      " abajo
}
#centro
MASTER_INDEX = 2