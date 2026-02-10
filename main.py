import sys
from src.utils.constants import PLAYER_RED, PLAYER_BLUE, Colors
from src.logic.game_engine import GameEngine

def main():
    print(f"{Colors.BOLD}=== ONITAMA: MOTOR DE JUEGO ACTIVADO ==={Colors.RESET}")
    
    # inicia el juego
    game = GameEngine()
    
    turn_count = 1
    
    while not game.winner:
        try:
            #pantalla
            print("\n" + "="*30)
            print(f"{Colors.BOLD}RONDA {turn_count}{Colors.RESET}")
            print(f"Turno de: {Colors.RED_TXT if game.current_turn == PLAYER_RED else Colors.BLUE_TXT}{game.current_turn}{Colors.RESET}")
            
            #Mostrar Tablero
            print(game.board)
            
            #Mostrar Cartas del Jugador Actual
            current_hand = game.red_hand if game.current_turn == PLAYER_RED else game.blue_hand
            print(f"Tu Mano: {current_hand}")
            print(f"{Colors.YELLOW_TXT}Carta en Mesa (Extra): {game.extra_card}{Colors.RESET}")

            #simulacion de juego
            print("\nMOVIMIENTO SIMULADO:")
            print("1. Seleccionando la primera carta de tu mano...")
            print("2. Intercambiando con la mesa...")
            
            cmd = input(f"\nPresiona ENTER para ejecutar turno o 'q' para salir: ")
            
            if cmd.lower() == 'q':
                break

            # Ejecutamos un "movimiento fantasma" (start=None, end=None) 
            # solo para probar que la rotación de cartas y turnos funciona.
            # Usamos el índice 0 de la mano.
            game.execute_move((0,0), (0,0), 0) 
            
            turn_count += 1

        except KeyboardInterrupt:
            print(f"\n{Colors.YELLOW_TXT}Saliendo...{Colors.RESET}")
            sys.exit(0)
        except Exception as e:
            print(f"{Colors.RED_TXT}Error en el Game Engine: {e}{Colors.RESET}")
            break

    if game.winner:
        print(f"\n{Colors.GREEN_TXT}¡PARTIDA TERMINADA! GANADOR: {game.winner}{Colors.RESET}")

if __name__ == "__main__":
    main()