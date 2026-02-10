from src.logic.board import Board
from src.utils.constants import BLUE, RED, ROWS, COLS

class Game:
    def __init__(self):
        self.board = Board()  # Instanciamos el tablero (Persona 3)
        self.turn = BLUE      # Por defecto empieza Azul (o quien diga la 5ta carta)
        
        # Estado de las cartas (Esto se llenará al iniciar la partida)
        # Formato: {BLUE: [Carta1, Carta2], RED: [Carta3, Carta4]}
        self.player_hands = {BLUE: [], RED: []} 
        self.side_card = None # La 5ta carta en espera

    def set_cards(self, cards):
        """
        Recibe las 5 cartas barajadas y las reparte.
        cards: Lista de 5 objetos Card.
        """
        self.player_hands[BLUE] = [cards[0], cards[1]]
        self.player_hands[RED] = [cards[2], cards[3]]
        self.side_card = cards[4]
        
        # En Onitama real, empieza quien tenga el color de la 5ta carta
        # Asumimos que la carta tiene un atributo 'color' (Persona 2)
        # Si no, déjalo por defecto en BLUE.
        if hasattr(self.side_card, 'color'):
             self.turn = self.side_card.color

    def switch_turn(self):
        """Alterna el turno entre Azul y Rojo"""
        if self.turn == BLUE:
            self.turn = RED
        else:
            self.turn = BLUE

    def card_rotation(self, card_index):
        """
        La mecánica única de Onitama:
        Intercambia la carta usada por el jugador con la 'side_card'.
        card_index: 0 o 1 (la carta de la izquierda o derecha de su mano)
        """
        # 1. Tomamos la carta que el jugador quiere usar
        used_card = self.player_hands[self.turn][card_index]
        
        # 2. Guardamos temporalmente la carta que estaba en la mesa (side_card)
        previous_side_card = self.side_card
        
        # 3. Ponemos la carta usada en la mesa
        self.side_card = used_card
        
        # 4. Le damos al jugador la carta que estaba en la mesa (en el mismo hueco)
        self.player_hands[self.turn][card_index] = previous_side_card

    def check_winner(self):
        """
        Verifica las dos condiciones de victoria:
        1. Vía de la Piedra: Capturar al maestro enemigo.
        2. Vía del Arroyo: Tu maestro llega al templo enemigo.
        Retorna: El color del ganador (BLUE/RED) o None si nadie ha ganado.
        """
        
        # --- CONDICIÓN 1: Vía de la Piedra (El maestro oponente no está en el tablero) ---
        # Le preguntamos al tablero si los maestros siguen vivos
        # Asumimos que board tiene un método o propiedad para esto.
        blue_alive = self.board.is_master_alive(BLUE)
        red_alive = self.board.is_master_alive(RED)

        if not blue_alive:
            return RED
        if not red_alive:
            return BLUE

        # --- CONDICIÓN 2: Vía del Arroyo (Ocupar el templo enemigo) ---
        # Templo Azul suele ser (0, 2) [si Azul empieza abajo]
        # Templo Rojo suele ser (4, 2) [si Rojo empieza arriba]
        # Esto depende de cómo Persona 3 defina el tablero, asumiremos coordenadas estándar.
        
        blue_temple_pos = (ROWS - 1, 2) # Fila 4, Columna 2
        red_temple_pos = (0, 2)         # Fila 0, Columna 2

        # ¿Hay un maestro Azul en el templo Rojo?
        piece_at_red_temple = self.board.get_piece_at(red_temple_pos)
        if piece_at_red_temple and piece_at_red_temple.is_master and piece_at_red_temple.color == BLUE:
            return BLUE

        # ¿Hay un maestro Rojo en el templo Azul?
        piece_at_blue_temple = self.board.get_piece_at(blue_temple_pos)
        if piece_at_blue_temple and piece_at_blue_temple.is_master and piece_at_blue_temple.color == RED:
            return RED

        return None

    def make_move(self, start_pos, end_pos, card_index):
        """
        El método principal que la UI llamará.
        1. Mueve la pieza en el tablero.
        2. Rota las cartas.
        3. Verifica victoria.
        4. Cambia turno.
        """
        # AQUI OCURRE LA MAGIA
        
        # 1. Ejecutar movimiento físico (Delegamos a Persona 3)
        self.board.move_piece(start_pos, end_pos)
        
        # 2. Rotación de cartas (Tu lógica)
        self.card_rotation(card_index)
        
        # 3. Verificar si alguien ganó
        winner = self.check_winner()
        if winner:
            return winner # La UI debe manejar el fin del juego
        
        # 4. Si nadie ganó, pasamos el turno
        self.switch_turn()
        return None
