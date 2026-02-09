
def get_player_move():
    """
    Pregunta al jugador qué quiere mover.
    Retorna las coordenadas de origen y destino.
    """
    print("\n--- TU TURNO ---")
    try:
        # Ejemplo: El usuario escribe '0 2'
        origin = input("Elige la pieza (fila columna): ").split()
        target = input("A donde la mueves (fila columna): ").split()
        
        # Convertimos a números para que el compañero "El arbitro" los use
        origin_coords = (int(origin[0]), int(origin[1]))
        target_coords = (int(target[0]), int(target[1]))
        
        return origin_coords, target_coords
    except:
        print("¡Error! Debes ingresar dos números separados por un espacio.")
        return None

def select_card(available_cards):
    """Muestra las cartas y deja elegir una"""
    print("\nCartas disponibles:")
    for i, card in enumerate(available_cards):
        print(f"{i}: {card}")
    
    choice = input("Elige el número de la carta: ")
    return int(choice)