import sys
#constantes
from src.utils.constants import PLAYER_RED, PLAYER_BLUE, Colors

# para las otras clases decomentar
# from src.logic.game_engine import OnitamaGame
# from src.ui.display import print_board
# from src.ui.input import get_player_move

def main():
    """
    Función principal. Inicializa el juego y corre el bucle principal.
    """
    print(f"{Colors.BOLD}=== INICIANDO ONITAMA ==={Colors.RESET}")
    
    # 1. Inicialización
    turn_count = 0
    is_running = True
    current_player = PLAYER_RED #empieza rojo

    # 2. Bucle
    while is_running:
        try:
            # mostrar donde esta
            print(f"\n--- Turno {turn_count}: Juega {current_player} ---")
            # imprime board
            print("(Aquí iría el tablero dibujado)")

            # B. jugada
            print(f"Esperando input de {current_player}... (Simulado)")
            
            cmd = input("Presiona ENTER para avanzar turno o 'q' para salir: ")
            if cmd.lower() == 'q':
                is_running = False
                break

            # C. Update (Actualizar lógica)
            # if game.apply_move(move):
            #     check_win_condition()
            #     switch_turn()
            
            # Simulación de cambio de turno
            current_player = PLAYER_BLUE if current_player == PLAYER_RED else PLAYER_RED
            turn_count += 1

        except KeyboardInterrupt:
            print(f"\n{Colors.YELLOW_TXT}Juego interrumpido por el usuario.{Colors.RESET}")
            sys.exit(0)
        except Exception as e:
            print(f"{Colors.RED_TXT}Error crítico: {e}{Colors.RESET}")
            # En producción, aquí harías un log del error
            break

    print("Gracias por jugar.")

if __name__ == "__main__":
    main()