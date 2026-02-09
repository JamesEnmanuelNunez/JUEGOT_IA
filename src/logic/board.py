from logic.piece import Piece

BOARD_SIZE = 5

class Board:
    def _init_(self):
        self.grid = [[None for _ in range(BOARD_SIZE)]
for _ in range(BOARD_SIZE)]
        self.initialize_board()

    def initialize_board(self):
    
        self.grid[0] = [
            Piece("B", "ESTUDIANTE"),
            Piece("B", "ESTUDIANTE"),
            Piece("B", "MAESTRO"),
            Piece("B", "ESTUDIANTE"),
            Piece("B", "ESTUDIANTE"),
        ]

        self.grid[4] = [
            Piece("R", "ESTUDIANTE"),
            Piece("R", "ESTUDIANTE"),
            Piece("R", "MAESTRO"),
            Piece("R", "ESTUDIANTE"),
            Piece("R", "ESTUDIANTE"),
        ]

    def print_board(self):
        print("\n  0 1 2 3 4")
        for i, row in enumerate(self.grid):
            print(i, end=" ")
            for cell in row:
                print(str(cell) if cell else ".", end=" ")
            print()