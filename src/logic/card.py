class Card:
    """
    Representa una carta de movimiento en el juego Onitama.

    Los movimientos se interpretan como desplazamientos relativos (dx, dy)
    sobre la matriz del tablero.

    - dx representa el cambio en la fila:
        * dx negativo  -> movimiento hacia adelante (hacia el rival)
        * dx positivo  -> movimiento hacia atrás

    - dy representa el cambio en la columna:
        * dy negativo  -> movimiento hacia la izquierda
        * dy positivo  -> movimiento hacia la derecha

    IMPORTANTE:
     esto solo son los movimiento basada desde la perspectiva del jugador
    que está en turno. Persona 4: El Árbitro (Logic - Game Engine) es el responsable de invertir
    los valores de dx cuando el movimiento pertenece al jugador contrario.
    """

    def __init__(self, name, moves):
        self.name = name
        self.moves = moves  # lista de tuplas (dx, dy)

    def __repr__(self):
        return f"Card({self.name})"


# Diccionario con las 16 cartas oficiales del juego Onitama.
# Cada carta contiene una lista de movimientos relativos (dx, dy),
CARDS = {

    "TIGER": Card("Tiger", [
        (-2, 0),   # Salta dos casillas hacia adelante
        (1, 0)     # Retrocede una casilla
    ]),

    "DRAGON": Card("Dragon", [
        (-1, -2),  # Adelante izquierda (largo)
        (-1, 2),   # Adelante derecha (largo)
        (1, -1),   # Atrás izquierda
        (1, 1)     # Atrás derecha
    ]),

    "CRAB": Card("Crab", [
        (0, -2),   # Movimiento lateral largo a la izquierda
        (0, 2),    # Movimiento lateral largo a la derecha
        (-1, 0)    # Avanza una casilla
    ]),

    "ELEPHANT": Card("Elephant", [
        (-1, -1),  # Adelante izquierda
        (-1, 1),   # Adelante derecha
        (0, -1),   # Lateral izquierda
        (0, 1)     # Lateral derecha
    ]),

    "MANTIS": Card("Mantis", [
        (-1, -1),  # Adelante izquierda
        (-1, 1),   # Adelante derecha
        (1, 0)     # Retrocede una casilla
    ]),

    "MONKEY": Card("Monkey", [
        (-1, -1),  # Adelante izquierda
        (-1, 1),   # Adelante derecha
        (1, -1),   # Atrás izquierda
        (1, 1)     # Atrás derecha
    ]),

    "CRANE": Card("Crane", [
        (-1, 0),   # Avanza una casilla
        (1, -1),   # Atrás izquierda
        (1, 1)     # Atrás derecha
    ]),

    "BOAR": Card("Boar", [
        (-1, 0),   # Avanza una casilla
        (0, -1),   # Lateral izquierda
        (0, 1)     # Lateral derecha
    ]),

    "FROG": Card("Frog", [
        (0, -2),   # Salto lateral largo a la izquierda
        (-1, -1),  # Adelante izquierda
        (1, 1)     # Atrás derecha
    ]),

    "RABBIT": Card("Rabbit", [
        (0, 2),    # Salto lateral largo a la derecha
        (-1, 1),   # Adelante derecha
        (1, -1)    # Atrás izquierda
    ]),

    "GOOSE": Card("Goose", [
        (0, -1),   # Lateral izquierda
        (-1, -1),  # Adelante izquierda
        (0, 1),    # Lateral derecha
        (1, 1)     # Atrás derecha
    ]),

    "ROOSTER": Card("Rooster", [
        (0, 1),    # Lateral derecha
        (-1, 1),   # Adelante derecha
        (0, -1),   # Lateral izquierda
        (1, -1)    # Atrás izquierda
    ]),

    "EEL": Card("Eel", [
        (-1, -1),  # Adelante izquierda
        (1, -1),   # Atrás izquierda
        (0, 1)     # Lateral derecha
    ]),

    "COBRA": Card("Cobra", [
        (-1, 1),   # Adelante derecha
        (1, 1),    # Atrás derecha
        (0, -1)    # Lateral izquierda
    ]),

    "HORSE": Card("Horse", [
        (-1, 0),   # Avanza una casilla
        (1, 0),    # Retrocede una casilla
        (0, -1)    # Lateral izquierda
    ]),

    "OX": Card("Ox", [
        (-1, 0),   # Avanza una casilla
        (1, 0),    # Retrocede una casilla
        (0, 1)     # Lateral derecha
    ]),
}
