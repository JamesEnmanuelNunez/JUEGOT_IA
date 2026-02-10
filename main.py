from src.logic.game_engine import GameEngine
from src.ui.display import draw_board, draw_card_map
from src.ui.input import get_player_move, select_card_index
from src.utils.constants import Colors

def main():
    game = GameEngine()
    print(f"{Colors.BOLD}=== ONITAMA MVP CARGADO ==={Colors.RESET}")

    while not game.winner:
        draw_board(game.board)
        
        current_hand = game.red_hand if game.current_turn == 'RED' else game.blue_hand
        print(f"\nTurno de: {game.current_turn}")
        print(f"Carta Extra: {game.extra_card.name}")
        
        # salir al elegir carta
        idx = select_card_index(current_hand)
        if idx is None: 
            print("\n Saliendo del juego. ¡Hasta la próxima!")
            break
            
        draw_card_map(current_hand[idx])

        # salir al  mover
        move_data = get_player_move()
        if move_data is None:
            print("\n Saliendo del juego. ¡Hasta la próxima!")
            break
            
        start, end = move_data

        # Intentar mover
        success = game.execute_move(start, end, idx)
        if not success:
            print(f"\n{Colors.RED_TXT} Movimiento no permitido.{Colors.RESET}")

    if game.winner:
        print(f"\n ¡EL JUGADOR {game.winner} HA GANADO!")

if __name__ == "__main__":
    main()