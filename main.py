from src.logic.ai_agent import MinimaxAgent
from src.logic.game_engine import GameEngine
from src.ui.display import draw_board, draw_card_map
from src.ui.input import get_player_move, select_card_index
from src.utils.constants import Colors
from src.ui.input import get_player_move, select_card_index, setup_menu

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
    game = GameEngine()
    print(f"{Colors.BOLD}=== ONITAMA MVP CARGADO ==={Colors.RESET}")

while True: #buble para las partidas
    #llamamos menu
    config = setup_menu()

    #inicio del motor
    game= GameEngine(config)

    print(f"\n{Colors.BOLD}!Comienza el Juego!{Colors.RESET}\n")

    while not game.winner:
        draw_board(game.board)
        
        #evaluacion de quien es el turno
        current_player_type = config[game.current_turn] #ahi sabemos si es el jugador o el bot o ia

        if current_player_type =="HUMAN":

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

        else:
            # ia va a tirar un mensaje de pensando por ahir
                    print(f"\nLa IA ({game.current_turn}) está pensando por un máximo de {config['ai_max_time']} segundos...")
                    # Aquí en el futuro llamaremos a best mode
                    break #rompemos bucle
                
    # jugar de nuevo
    play_again = input("\n¿Desean jugar otra partida? (S/N): ").strip().upper()
    if play_again != 'S':
        print("\nSaliendo del juego. ¡Hasta la próxima!")
        break


        start, end = move_datad
        
        success = game.execute_move(start, end, idx)
        if not success:
            print(f"\n{Colors.RED_TXT} Movimiento no permitido.{Colors.RESET}")

#     if game.winner:
#         print(f"\n ¡EL JUGADOR {game.winner} HA GANADO!")

# if __name__ == "__main__":
#     main()