from typing import List, Tuple, Optional
from src.logic.board import Board
from src.logic.card import Card, deal_cards
from src.utils.constants import PLAYER_RED, PLAYER_BLUE, ROWS, COLS, PIECE_MASTER

class Move:
    """Clase simple para empaquetar los datos de un movimiento para la IA."""
    def __init__(self, start: Tuple[int, int], end: Tuple[int, int], card_idx: int):
        self.start = start
        self.end = end
        self.card_idx = card_idx

class GameEngine:
    def __init__(self, config=None):


        self.config = config if config is not None else {}

        #componentes del board 
        self.board = Board()
        
        # 2. Estado de las cartas 
        # deal_cards para iniciar la partida
        self.red_hand, self.blue_hand, self.extra_card = deal_cards()
        
        # 3. El turno inicial lo define la carta extra (Regla de Oro)
        self.current_turn = self.extra_card.color
        self.winner: Optional[str] = None

    def switch_turn(self):
        """Cambia el turno entre RED y BLUE."""
        self.current_turn = PLAYER_BLUE if self.current_turn == PLAYER_RED else PLAYER_RED

    def _is_master_alive(self, color: str) -> bool:
        """Escanea el tablero para ver si el maestro de un color sigue en pie."""
        for r in range(ROWS):
            for c in range(COLS):
                piece = self.board.get_piece(r, c)
                if piece and piece.color == color and piece.kind == PIECE_MASTER:
                    return True
        return False

    def check_winner(self) -> Optional[str]:
        """Verifica condiciones de victoria de Onitama."""
        # Vía de la Piedra: Capturar al maestro
        if not self._is_master_alive(PLAYER_BLUE): return PLAYER_RED
        if not self._is_master_alive(PLAYER_RED): return PLAYER_BLUE

        # Vía del Arroyo: Maestro llega al templo enemigo
        # Templo Azul (fila 4, col 2) | Templo Rojo (fila 0, col 2)
        red_temple = self.board.get_piece(0, 2)
        if red_temple and red_temple.kind == PIECE_MASTER and red_temple.color == PLAYER_BLUE:
            return PLAYER_BLUE

        blue_temple = self.board.get_piece(4, 2)
        if blue_temple and blue_temple.kind == PIECE_MASTER and blue_temple.color == PLAYER_RED:
            return PLAYER_RED

        return None

    def execute_move(self, start_pos: Tuple[int, int], end_pos: Tuple[int, int], card_index: int) -> bool:
        """
        Ejecuta la jugada completa si es válida.
        card_index: 0 o 1 (la carta de la mano del jugador actual)
        """
        r_s, c_s = start_pos
        r_e, c_e = end_pos
        
        #tener mano actual
        hand = self.red_hand if self.current_turn == PLAYER_RED else self.blue_hand
        if not (0 <= card_index < len(hand)): return False
        
        selected_card = hand[card_index]

        
        # 2. Mover físicamente en la matriz
        piece_to_move = self.board.grid[r_s][c_s]
        self.board.grid[r_e][c_e] = piece_to_move
        self.board.grid[r_s][c_s] = None

        # 3. Rotación de cartas 
        if self.current_turn == PLAYER_RED:
            self.red_hand[card_index], self.extra_card = self.extra_card, self.red_hand[card_index]
        else:
            self.blue_hand[card_index], self.extra_card = self.extra_card, self.blue_hand[card_index]

        # 4. Verificar victoria y cambiar turno
        self.winner = self.check_winner()
        if not self.winner:
            self.switch_turn()
            
        return True
    
    def get_all_legal_moves(self, color: str) -> List[Move]:
        """Genera una lista con todos los movimientos válidos para un color dado."""
        legal_moves = []
        hand = self.red_hand if color == PLAYER_RED else self.blue_hand
        
        # 1. Escanear todo el tablero buscando piezas del color que tiene el turno
        for r in range(ROWS):
            for c in range(COLS):
                piece = self.board.grid[r][c]
                
                if piece is not None and piece.color == color:
                    start_pos = (r, c)
                    
                    # 2. Por cada pieza, probamos las 2 cartas en la mano
                    for card_idx, card in enumerate(hand):
                        
                        # (Nota: Asumo que en tu card.py tienes una lista de tuplas llamada 'moves')
                        for dr, dc in card.moves: 
                            
                            # 3. Ajustar la dirección según el bando (RED sube, BLUE baja)
                            if color == PLAYER_RED:
                                target_r = r - dr
                                target_c = c + dc
                            else:
                                target_r = r + dr
                                target_c = c - dc
                                
                            # 4. Verificar que el destino no se salga del tablero (5x5)
                            if 0 <= target_r < ROWS and 0 <= target_c < COLS:
                                target_piece = self.board.grid[target_r][target_c]
                                
                                # 5. El movimiento es legal si la casilla está vacía o tiene un enemigo
                                if target_piece is None or target_piece.color != color:
                                    end_pos = (target_r, target_c)
                                    legal_moves.append(Move(start_pos, end_pos, card_idx))
                                    
        return legal_moves