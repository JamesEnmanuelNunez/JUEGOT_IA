import time
import copy

class TimeoutException(Exception):
    """Excepción para detener la búsqueda cuando se acaba el tiempo."""
    pass

class MinimaxAgent:
    def __init__(self, ai_color):
        self.ai_color = ai_color # BLUE o RED

    def get_best_move(self, game_state, max_time):
        """
        Inicia la Búsqueda de Profundidad Iterativa (IDS).
        """
        start_time = time.time()
        best_move_overall = None
        depth = 1

        try:
            # IDS: Profundizamos cada vez más hasta que salte la alarma de tiempo
            while (time.time() - start_time) < max_time:
                # Calculamos el mejor movimiento para la profundidad actual
                score, current_best_move = self.minimax(
                    game_state, depth, float('-inf'), float('inf'), True, start_time, max_time
                )
                
                # Si terminamos esta profundidad sin quedarnos sin tiempo, lo guardamos
                if current_best_move:
                    best_move_overall = current_best_move
                
                depth += 1 # Vamos un nivel más profundo para la siguiente iteración

        except TimeoutException:
            # ¡Se acabó el tiempo a mitad de un cálculo profundo!
            # No importa, devolvemos el mejor movimiento que encontramos en la profundidad anterior.
            print(f"[IA] Pensamiento detenido. Profundidad completada: {depth - 1}")

        return best_move_overall

    def minimax(self, game_state, depth, alpha, beta, maximizing_player, start_time, max_time):
        """
        El núcleo: Minimax con Poda Alfa-Beta.
        """
        # 1. Vigilar el reloj (Si nos pasamos, abortamos)
        if time.time() - start_time >= max_time:
            raise TimeoutException()

        # 2. Casos Base: Llegamos al límite de profundidad o el juego se acabó
        winner = game_state.winner # Asumimos que game_engine actualiza esta variable
        if depth == 0 or winner is not None:
            return self._basic_heuristic(game_state, winner), None

        # 3. Obtener todos los movimientos posibles
        current_color = self.ai_color if maximizing_player else self._get_opponent_color()
        
        # OJO: Esta función debe existir en GameEngine
        legal_moves = game_state.get_all_legal_moves(current_color)

        if not legal_moves:
            return self._basic_heuristic(game_state, winner), None

        best_move = None

        # 4. Turno de la IA (Maximizar su ventaja)
        if maximizing_player:
            max_eval = float('-inf')
            for move in legal_moves:
                # Simular el futuro
                simulated_game = copy.deepcopy(game_state) 
                simulated_game.execute_move(move.start, move.end, move.card_idx)

                # Recursión (ahora le toca al oponente, así que False)
                eval_score, _ = self.minimax(simulated_game, depth - 1, alpha, beta, False, start_time, max_time)

                if eval_score > max_eval:
                    max_eval = eval_score
                    best_move = move

                # Poda Alfa-Beta
                alpha = max(alpha, eval_score)
                if beta <= alpha:
                    break # Cortar rama inútil
            return max_eval, best_move

        # 5. Turno del Oponente Humano (Minimizar la ventaja de la IA)
        else:
            min_eval = float('inf')
            for move in legal_moves:
                # Simular el futuro
                simulated_game = copy.deepcopy(game_state)
                simulated_game.execute_move(move.start, move.end, move.card_idx)

                # Recursión (ahora le toca a la IA, así que True)
                eval_score, _ = self.minimax(simulated_game, depth - 1, alpha, beta, True, start_time, max_time)

                if eval_score < min_eval:
                    min_eval = eval_score
                    best_move = move

                # Poda Alfa-Beta
                beta = min(beta, eval_score)
                if beta <= alpha:
                    break # Cortar rama inútil
            return min_eval, best_move

    def _basic_heuristic(self, game_state, winner):
        """
        Función temporal para evaluar qué tan bueno es un tablero.
        La persona de la Parte 3 cambiará esto por una heurística avanzada.
        """
        if winner == self.ai_color:
            return 10000 # Ganamos
        elif winner == self._get_opponent_color():
            return -10000 # Perdimos
            
        return 0 # Empate temporal para que el código no falle

    def _get_opponent_color(self):
        return 'RED' if self.ai_color == 'BLUE' else 'BLUE'