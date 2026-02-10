
from typing import List, Optional
# Import
from src.logic.piece import Piece
from src.utils.constants import ROWS, COLS, PLAYER_RED, PLAYER_BLUE, START_POSITIONS, PIECE_MASTER, PIECE_STUDENT

class Board:
    def __init__(self):
        # Matriz 5x5 
        self.grid: List[List[Optional[Piece]]] = [[None for _ in range(COLS)] for _ in range(ROWS)]
        self._initialize_pieces()

    def _initialize_pieces(self):
        """Coloca las piezas en sus posiciones iniciales."""
        # Colocar Rojas
        for idx, (r, c) in enumerate(START_POSITIONS[PLAYER_RED]):
            kind = PIECE_MASTER if idx == 2 else PIECE_STUDENT
            self.grid[r][c] = Piece(PLAYER_RED, kind)

        # Colocar Azules
        for idx, (r, c) in enumerate(START_POSITIONS[PLAYER_BLUE]):
            kind = PIECE_MASTER if idx == 2 else PIECE_STUDENT
            self.grid[r][c] = Piece(PLAYER_BLUE, kind)

    def get_piece(self, row: int, col: int) -> Optional[Piece]:
        if 0 <= row < ROWS and 0 <= col < COLS:
            return self.grid[row][col]
        return None

    def __str__(self):
        board_str = "   0   1   2   3   4\n"
        board_str += "  -------------------\n"
        for r in range(ROWS):
            board_str += f"{r} |"
            for c in range(COLS):
                piece = self.grid[r][c]
                cell = f" {piece.color[0]}{piece.kind[0]} " if piece else " . "
                board_str += cell + "|"
            board_str += "\n  -------------------\n"
        return board_str

