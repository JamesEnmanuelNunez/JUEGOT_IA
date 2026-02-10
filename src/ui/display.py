from src.utils.constants import PLAYER_RED, PLAYER_BLUE, Colors
from src.logic.board import Board

def draw_board(board: Board):
    """
    Dibuja el tablero usando los objetos Piece reales.
    """
    print("\n      0     1     2     3     4")
    print("   " + "o-----" * 5 + "o")
    
    for r in range(5):
        row_str = f" {r} |"
        for c in range(5):
            piece = board.get_piece(r, c)
            if piece is None:
                display_char = "  .  "
            elif piece.color == PLAYER_RED:
                # Equipo Rojo con brillo (negrita)
                display_char = f" {Colors.RED_TXT}{piece.kind[0]}* {Colors.RESET}"
            else:
                # Equipo Azul entre paréntesis
                display_char = f" {Colors.BLUE_TXT}({piece.kind[0]}){Colors.RESET}"
            row_str += f"{display_char}|"
        
        print(row_str)
        print("   " + "o-----" * 5 + "o")

def draw_card_map(card):
    """
    Dibuja un mapa visual de 5x5 para la carta seleccionada.
    """
    print(f"\n{Colors.BOLD}MAPA DE MOVIMIENTO: {card.name}{Colors.RESET}")
    grid = [["." for _ in range(5)] for _ in range(5)]
    center = 2
    grid[center][center] = "H" # Tu pieza (Home)
    
    for dr, dc in card.moves:
        # dr y dc son los deltas que definimos en card.py
        target_r = center + dr
        target_c = center + dc
        if 0 <= target_r < 5 and 0 <= target_c < 5:
            grid[target_r][target_c] = f"{Colors.GREEN_TXT}X{Colors.RESET}"
        
    for row in grid:
        print("  " + " ".join(row))
    print(" (H=Pieza, X=Destino)")