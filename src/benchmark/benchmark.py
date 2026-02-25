import csv
import time
import copy
from src.logic.game_engine import GameEngine
from src.logic.ai_agent import MinimaxAgent
from src.ai.opponents import RandomBot, GreedyBot, WorstBot

class Benchmark:
    def __init__(self):
        self.results = []

    def run_match(self, red_bot, blue_bot, label):
        # Iniciamos un motor limpio para cada partida
        engine = GameEngine()
        start_time = time.time()
        
        # Límite de seguridad de movimientos para evitar bucles infinitos
        max_moves = 200 
        move_count = 0

        while not engine.winner and move_count < max_moves:
            current_agent = red_bot if engine.current_turn == "RED" else blue_bot
            
            # Pedir movimiento al bot
            # Pasamos 3 segundos por defecto si no es Minimax
            move = current_agent.get_best_move(engine, 3) 

            if move is None:
                break

            engine.execute_move(move.start, move.end, move.card_idx)
            move_count += 1

        total_time = time.time() - start_time

        result = {
            "Configuracion": label,
            "Ganador": engine.winner if engine.winner else "Empate/Timeout",
            "Piezas_Rojas": self.count_pieces(engine, "RED"),
            "Piezas_Azules": self.count_pieces(engine, "BLUE"),
            "Duracion_Partida": round(total_time, 4),
            "Total_Movimientos": move_count
        }
        self.results.append(result)
        print(f" Partida finalizada: {label} -> Ganador: {engine.winner}")

    def count_pieces(self, engine, color):
        count = 0
        for row in engine.board.grid:
            for piece in row:
                if piece and piece.color == color:
                    count += 1
        return count

    def export_csv(self, filename="resultados_onitama.csv"):
        if not self.results: return
        with open(filename, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=self.results[0].keys())
            writer.writeheader()
            writer.writerows(self.results)
        print(f"\n✅ Laboratorio terminado. Datos guardados en '{filename}'")

if __name__ == "__main__":
    lab = Benchmark()
    
    # 1. Definimos los contrincantes
    print(" Iniciando simulaciones de laboratorio...")
    
    # Pruebas: 5 partidas por cada configuración
    configs = [
        (MinimaxAgent("RED"), RandomBot("BLUE"), "Minimax vs Random"),
        (MinimaxAgent("RED"), GreedyBot("BLUE"), "Minimax vs Greedy"),
        (MinimaxAgent("RED"), WorstBot("BLUE"), "Minimax vs WorstBot"),
        (MinimaxAgent("RED"), MinimaxAgent("BLUE"), "Minimax vs Minimax")
    ]

    for red, blue, label in configs:
        for i in range(5): # Hacemos 5 repeticiones
            lab.run_match(red, blue, f"{label} (Intento {i+1})")

    lab.export_csv()