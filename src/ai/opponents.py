import random
import copy
from src.logic.Heuristicas import Evaluador

class RandomBot:
    """Bot 1: Toma decisiones completamente al azar."""
    def __init__(self, ai_color):
        self.ai_color = ai_color

    def get_best_move(self, game_state, max_time=None):
        # 1. Usamos la función OFICIAL de tu motor
        legal_moves = game_state.get_all_legal_moves(self.ai_color)
        if not legal_moves:
            return None
        # 2. Retornamos un objeto Move (compatible con Minimax)
        return random.choice(legal_moves)


class GreedyBot:
    """Bot 2: El avaro. Busca capturar o ganar la mayor cantidad de puntos de inmediato."""
    def __init__(self, ai_color):
        self.ai_color = ai_color
        self.evaluador = Evaluador()

    def get_best_move(self, game_state, max_time=None):
        legal_moves = game_state.get_all_legal_moves(self.ai_color)
        if not legal_moves:
            return None

        best_move = random.choice(legal_moves) # Por si todos dan 0
        best_score = float('-inf')

        for move in legal_moves:
            simulated_game = copy.deepcopy(game_state)
            simulated_game.execute_move(move.start, move.end, move.card_idx)
            
            score = self.evaluador(simulated_game, self.ai_color)
            
            if score > best_score:
                best_score = score
                best_move = move
                
        return best_move


class WorstBot:
    """Bot 3: El suicida. Toma a propósito la peor decisión posible."""
    def __init__(self, ai_color):
        self.ai_color = ai_color
        self.evaluador = Evaluador()

    def get_best_move(self, game_state, max_time=None):
        legal_moves = game_state.get_all_legal_moves(self.ai_color)
        if not legal_moves:
            return None

        worst_move = random.choice(legal_moves)
        worst_score = float('inf') # Buscamos el número más pequeño

        for move in legal_moves:
            simulated_game = copy.deepcopy(game_state)
            simulated_game.execute_move(move.start, move.end, move.card_idx)
            
            score = self.evaluador(simulated_game, self.ai_color)
            
            # Si el puntaje es menor, es una peor jugada (¡Lo que buscamos!)
            if score < worst_score:
                worst_score = score
                worst_move = move
                
        return worst_move