from typing import Tuple, Optional
from src.utils.constants import Colors

def get_player_move() -> Optional[Tuple[Tuple[int, int], Tuple[int, int]]]:
    """
    Pide coordenadas. Si el usuario escribe 'q', devuelve None para salir.
    """
    while True:
        try:
            print("\n(Escribe 'q' para salir del juego)")
            raw_origin = input("Elige pieza a mover (fila columna): ").lower().strip()
            if raw_origin == 'q': return None
            
            raw_target = input("A dónde la mueves (fila columna): ").lower().strip()
            if raw_target == 'q': return None
            
            origin_split = raw_origin.split()
            target_split = raw_target.split()

            if len(origin_split) != 2 or len(target_split) != 2:
                print(" Error: Ingresa dos números (ej: 4 2)")
                continue
                
            origin = (int(origin_split[0]), int(origin_split[1]))
            target = (int(target_split[0]), int(target_split[1]))
            
            return origin, target
        except ValueError:
            print(" Error: Solo números o 'q' para salir.")
        except KeyboardInterrupt:
            return None

def select_card_index(hand) -> Optional[int]:
    """Deja elegir carta o salir con 'q'."""
    while True:
        try:
            print("\nCartas en tu mano (escribe 'q' para salir):")
            for i, card in enumerate(hand):
                print(f"[{i}] - {card.name}")
            
            user_input = input("Selecciona [0] o [1]: ").lower().strip()
            if user_input == 'q': return None
            
            choice = int(user_input)
            if choice in [0, 1]:
                return choice
            print(" Error: Elige 0, 1 o 'q'.")
        except ValueError:
            print(" Error: Entrada inválida.")



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