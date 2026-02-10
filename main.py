import sys

# constantes
from src.utils.constants import PLAYER_RED, PLAYER_BLUE, Colors

# componentes
from src.logic.board import Board
from src.logic.card import deal_cards

def main():
    """
    Función principal. Inicializa el juego y prueba la integración de componentes.
    """
    print(f"{Colors.BOLD}=== INICIANDO ONITAMA (MODO DEPURACIÓN) ==={Colors.RESET}")
    
    # iniciar tableto
    print(f"\n{Colors.YELLOW_TXT}1. Generando Tablero y Piezas...{Colors.RESET}")
    board = Board()
    print(board)  
    
    # reparte cartas
    print(f"{Colors.YELLOW_TXT}2. Barajando y Repartiendo Cartas...{Colors.RESET}")
    red_hand, blue_hand, extra_card = deal_cards()
    
    # manos repartidas
    print(f"  🔴 Mano Roja:  {red_hand}")
    print(f"  🔵 Mano Azul:  {blue_hand}")
    print(f"  ⚪ Carta Mesa: {extra_card}")

    # turno
    current_player = extra_card.color
    
    print(f"\n{Colors.GREEN_TXT}>>> REGLA DE ORO: La carta extra es {extra_card.color}.{Colors.RESET}")
    print(f"{Colors.GREEN_TXT}>>> ¡EMPIEZA EL JUGADOR {current_player}!{Colors.RESET}")

    # bucle
    turn_count = 1
    is_running = True

    while is_running:
        try:
            print(f"\n--- Ronda {turn_count} | Turno de: {current_player} ---")
            
            # Aquí iría la lógica de pedir movimiento (input)
            # Como aún no tenemos Game Engine, solo pausamos para ver el resultado.
            
            cmd = input("Presiona ENTER para simular cambio de turno (o 'q' para salir): ")
            
            if cmd.lower() == 'q':
                print("Cerrando juego...")
                is_running = False
                break
            
            # Cambio de turno simple para probar el bucle
            current_player = PLAYER_BLUE if current_player == PLAYER_RED else PLAYER_RED
            turn_count += 1

        except KeyboardInterrupt:
            print(f"\n{Colors.YELLOW_TXT}Juego interrumpido.{Colors.RESET}")
            sys.exit(0)

if __name__ == "__main__":
    main()