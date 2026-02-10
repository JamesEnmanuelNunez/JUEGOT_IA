import random
from typing import List, Tuple, Dict

#constastes
from src.utils.constants import PLAYER_RED, PLAYER_BLUE

class Card:
    """
    Representa una carta de movimiento en Onitama.
    """
    def __init__(self, name: str, moves: List[Tuple[int, int]], color: str):
        """
        :param name: Nombre de la carta (ej. "Tiger")
        :param moves: Lista de movimientos [(d_row, d_col)]
        :param color: PLAYER_RED o PLAYER_BLUE (Determina inicio si es extra)
        """
        self.name = name
        self.moves = moves
        self.color = color

    def __repr__(self):
        #primera letra del color
        return f"[{self.name}|{self.color[0]}]"

# cartas
ALL_CARDS_LIST = [
    # rojas
    Card("Dragon", [(-1, -2), (-1, 2), (1, -1), (1, 1)], PLAYER_RED),
    Card("Frog",   [(-1, -1), (0, -2), (1, 1)], PLAYER_RED),
    Card("Rabbit", [(-1, 1), (0, 2), (1, -1)], PLAYER_RED),
    Card("Crab",   [(-1, 0), (0, -2), (0, 2)], PLAYER_RED),
    Card("Elephant",[(-1, 1), (-1, -1), (0, 1), (0, -1)], PLAYER_RED),
    Card("Goose",  [(-1, -1), (0, -1), (0, 1), (1, 1)], PLAYER_RED),
    Card("Rooster",[(-1, 1), (0, -1), (0, 1), (1, -1)], PLAYER_RED),
    Card("Monkey", [(-1, 1), (-1, -1), (1, 1), (1, -1)], PLAYER_RED),

    # azules
    Card("Tiger",  [(-2, 0), (1, 0)], PLAYER_BLUE),
    Card("Mantis", [(-1, 1), (-1, -1), (1, 0)], PLAYER_BLUE),
    Card("Horse",  [(-1, 0), (0, -1), (1, 0)], PLAYER_BLUE),
    Card("Ox",     [(-1, 0), (0, 1), (1, 0)], PLAYER_BLUE),
    Card("Crane",  [(-1, 0), (1, -1), (1, 1)], PLAYER_BLUE),
    Card("Boar",   [(-1, 0), (0, -1), (0, 1)], PLAYER_BLUE),
    Card("Eel",    [(-1, -1), (0, 1), (1, -1)], PLAYER_BLUE),
    Card("Cobra",  [(-1, 1), (0, -1), (1, 1)], PLAYER_BLUE)
]

def deal_cards() -> Tuple[List[Card], List[Card], Card]:
    """
    Baraja y reparte las cartas.
    Retorna: (mano_red, mano_blue, carta_extra)
    """
    # copia de lista
    deck = ALL_CARDS_LIST.copy()
    random.shuffle(deck)
    
    #reparte las 5 cartas
    red_hand = deck[0:2]
    blue_hand = deck[2:4]
    extra_card = deck[4]
    
    return red_hand, blue_hand, extra_card