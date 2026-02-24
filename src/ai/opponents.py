import random
from typing import Tuple, List

class TestBots:
    def __init__(self, engine):
        self.engine = engine # Aquí recibes el GameEngine de James

    def get_all_legal_moves(self) -> List[Tuple[Tuple[int, int], Tuple[int, int], int]]:
        """
        Genera todos los movimientos posibles para el turno actual.
        Retorna: [(inicio, fin, indice_carta), ...]
        """
        legal_moves = []
        hand = self.engine.red_hand if self.engine.current_turn == "RED" else self.engine.blue_hand
        
        # Recorremos el tablero buscando piezas del jugador actual
        for r in range(5):
            for c in range(5):
                piece = self.engine.board.get_piece(r, c)
                if piece and piece.color == self.engine.current_turn:
                    # Probamos las 2 cartas de la mano
                    for card_idx in range(len(hand)):
                        card = hand[card_idx]
                        # Aquí pedimos a la carta sus movimientos posibles
                        for move_offset in card.moves:
                            # Ajustar dirección si es Blue ellos miran hacia 'abajo'
                            direction = 1 if self.engine.current_turn == "RED" else -1
                            dr, dc = move_offset[0] * direction, move_offset[1] * direction
                            
                            end_r, end_c = r + dr, c + dc
                            
                            # Validar que esté en el tablero y no pise pieza propia
                            if 0 <= end_r < 5 and 0 <= end_c < 5:
                                target = self.engine.board.get_piece(end_r, end_c)
                                if target is None or target.color != self.engine.current_turn:
                                    legal_moves.append(((r, c), (end_r, end_c), card_idx))
        return legal_moves

    def random_bot(self):
        moves = self.get_all_legal_moves()
        return random.choice(moves) if moves else None

    def greedy_bot(self):
        moves = self.get_all_legal_moves()
        for start, end, idx in moves:
            target = self.engine.board.get_piece(end[0], end[1])
            # Si puede capturar al Maestro, es la prioridad máxima
            if target and target.kind == "MASTER":
                return (start, end, idx)
        # Si no, intenta capturar cualquier cosa
        for start, end, idx in moves:
            if self.engine.board.get_piece(end[0], end[1]) is not None:
                return (start, end, idx)
        return self.random_bot()