from src.logic.ai_agent import MinimaxAgent
from src.logic.game_engine import GameEngine
from src.ui.display import draw_board, draw_card_map
from src.ui.input import get_player_move, select_card_index
from src.utils.constants import Colors

def setup_menu():
    print(f"\n{Colors.BOLD}=== CONFIGURACIÓN DE LA PARTIDA ==={Colors.RESET}")
    num_players = input("Ingrese la cantidad de jugadores (Ej: 2): ")
    
    print("\nDefina quién controla cada bando (H = Humano, I = IA):")
    p1_type = input("Jugador 1 (RED) - ¿Humano o IA? [H/I]: ").strip().upper()
    p2_type = input("Jugador 2 (BLUE) - ¿Humano o IA? [H/I]: ").strip().upper()
    
    ai_time = 0
    if p1_type == 'I' or p2_type == 'I':
        ai_time_str = input("\nIngrese el tiempo máximo para la IA (en seg, ej: 3): ")
        ai_time = int(ai_time_str) if ai_time_str.isdigit() else 3
        
    return {
        "num_players": int(num_players) if num_players.isdigit() else 2,
        "RED": "HUMAN" if p1_type == 'H' else "AI",
        "BLUE": "HUMAN" if p2_type == 'H' else "AI",
        "ai_max_time": ai_time
    }

def main():
    print(f"{Colors.BOLD}=== ONITAMA MVP CARGADO ==={Colors.RESET}")

    while True: #bucle para las partidas
        #llamamos menu
        config = setup_menu()

        #inicio del motor
        game = GameEngine(config)

        print(f"\n{Colors.BOLD}!Comienza el Juego!{Colors.RESET}\n")

        while not game.winner:
            draw_board(game.board)
            
            #evaluacion de quien es el turno
            current_player_type = config[game.current_turn] #ahi sabemos si es el jugador o el bot o ia

            if current_player_type == "HUMAN":
                current_hand = game.red_hand if game.current_turn == 'RED' else game.blue_hand
                print(f"\nTurno de: {game.current_turn}")
                print(f"Carta Extra: {game.extra_card.name}")
                
                # salir al elegir carta
                idx = select_card_index(current_hand)
                if idx is None: 
                    print("\n Saliendo del juego. ¡Hasta la próxima!")
                    return # Salir completamente de la funcion main
                    
                draw_card_map(current_hand[idx])

                # salir al  mover
                move_data = get_player_move()
                if move_data is None:
                    print("\n Saliendo del juego. ¡Hasta la próxima!")
                    return # Salir completamente
                    
                start, end = move_data
                
                # EJECUTAR MOVIMIENTO HUMANO
                success = game.execute_move(start, end, idx)
                if not success:
                    print(f"\n{Colors.RED_TXT} Movimiento no permitido. Intenta de nuevo.{Colors.RESET}")

            else:
                # TURNO DE LA IA
                print(f"\nLa IA ({game.current_turn}) está pensando por un máximo de {config['ai_max_time']} segundos...")
                
                # 1. Instanciamos tu IA
                ia_agent = MinimaxAgent(ai_color=game.current_turn)
                
                # 2. Le pedimos a la IA que calcule
                best_move = ia_agent.get_best_move(game, config['ai_max_time'])
                
                # 3. Ejecutamos la decisión
                if best_move:
                    print(f"La IA decidió mover de {best_move.start} a {best_move.end}")
                    success = game.execute_move(best_move.start, best_move.end, best_move.card_idx)
                    
                    if not success:
                        print(f"\n{Colors.RED_TXT} Error de la IA: Movimiento no permitido.{Colors.RESET}")
                        break # Algo salió mal con la lógica de la IA
                else:
                    print("La IA no encontró movimientos válidos. Pierde su turno (o se rinde).")
                    break

        # REVISIÓN DE VICTORIA FUERA DEL BUCLE DE TURNOS
        if game.winner:
            draw_board(game.board) # Dibujar el tablero final
            print(f"\n{Colors.BOLD}¡EL JUGADOR {game.winner} HA GANADO!{Colors.RESET}")
                    
        # jugar de nuevo
        play_again = input("\n¿Desean jugar otra partida? (S/N): ").strip().upper()
        if play_again != 'S':
            print("\nSaliendo del juego. ¡Hasta la próxima!")
            break

if __name__ == "__main__":
    main()