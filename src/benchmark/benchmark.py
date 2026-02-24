import csv
import time
from src.logic.game_engine import GameEngine
from src.logic.test_bots import TestBots
from src.logic.ai.minimax_engine import MinimaxEngine


class Benchmark:

    def __init__(self):
        self.results = []

    def run_match(self, red_player, blue_player, label):

        engine = GameEngine()
        bots = TestBots(engine)

        start_time = time.time()

        while not engine.winner:

            if engine.current_turn == "RED":
                move = self.get_move(red_player, engine, bots)
            else:
                move = self.get_move(blue_player, engine, bots)

            if move is None:
                break

            start, end, idx = move
            engine.execute_move(start, end, idx)

        total_time = time.time() - start_time

        result = {
            "config": label,
            "winner": engine.winner,
            "red_pieces": self.count_pieces(engine, "RED"),
            "blue_pieces": self.count_pieces(engine, "BLUE"),
            "nodes_expanded": getattr(red_player, "nodes_expanded", 0),
            "depth_reached": getattr(red_player, "max_depth_reached", 0),
            "match_time": round(total_time, 4)
        }

        self.results.append(result)

    def get_move(self, player, engine, bots):

        if player == "random":
            return bots.random_bot()

        if player == "greedy":
            return bots.greedy_bot()

        if player == "worst":
            moves = bots.get_all_legal_moves()
            return moves[-1] if moves else None

        if isinstance(player, MinimaxEngine):
            return player.search(engine, engine.current_turn)

        return None

    def count_pieces(self, engine, color):
        count = 0
        for row in engine.board.grid:
            for piece in row:
                if piece and piece.color == color:
                    count += 1
        return count

    def export_csv(self, filename="benchmark_results.csv"):

        with open(filename, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=self.results[0].keys())
            writer.writeheader()
            writer.writerows(self.results)

        print(f"\nBenchmark terminado. Archivo '{filename}' generado.")


# ================================
# EJECUCIÓN PRINCIPAL
# ================================
if __name__ == "__main__":

    benchmark = Benchmark()

    times = [1, 3, 10]  # Configuraciones de tiempo

    for t in times:

        minimax = MinimaxEngine(max_time=t)

        # Minimax vs Random
        for i in range(10):
            benchmark.run_match(
                minimax,
                "random",
                f"Minimax({t}s) vs Random"
            )

        # Minimax vs Greedy
        for i in range(10):
            benchmark.run_match(
                minimax,
                "greedy",
                f"Minimax({t}s) vs Greedy"
            )

        # Minimax vs Worst
        for i in range(10):
            benchmark.run_match(
                minimax,
                "worst",
                f"Minimax({t}s) vs Worst"
            )

        # Minimax vs Minimax
        for i in range(10):
            minimax2 = MinimaxEngine(max_time=t)
            benchmark.run_match(
                minimax,
                minimax2,
                f"Minimax({t}s) vs Minimax({t}s)"
            )

    benchmark.export_csv()
