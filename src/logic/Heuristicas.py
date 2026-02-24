# PERSONA 3 — HEURÍSTICAS PARA ONITAMA (ADAPTADO AL GAME ENGINE)

# 1) Control del centro del tablero
def control_centro(state, player):
    opponent = 'BLUE' if player == 'RED' else 'RED'
    score = 0
    
    # Recorremos el grid (5x5)
    for r in range(5):
        for c in range(5):
            piece = state.board.grid[r][c]
            if piece is not None:
                # Calculamos distancia al centro exacto (2, 2)
                dist = abs(r - 2) + abs(c - 2)
                # Damos más puntos mientras más cerca del centro (máx 4)
                valor_posicion = 4 - dist 
                
                if piece.color == player:
                    score += valor_posicion
                elif piece.color == opponent:
                    score -= valor_posicion
    return score

# 2) Movilidad (cantidad de movimientos disponibles)
def movilidad(state, player):
    opponent = 'BLUE' if player == 'RED' else 'RED'
    # Usamos la función real de tu GameEngine
    mis_movimientos = len(state.get_all_legal_moves(player))
    sus_movimientos = len(state.get_all_legal_moves(opponent))
    return mis_movimientos - sus_movimientos

# 3) Progreso hacia el templo rival
def distancia_templo(state, player):
    opponent = 'BLUE' if player == 'RED' else 'RED'
    
    # Coordenadas clásicas de templos en Onitama (0,2 para Blue, 4,2 para Red)
    mi_templo = (4, 2) if player == 'RED' else (0, 2)
    templo_enemigo = (0, 2) if player == 'RED' else (4, 2)
    
    mi_master_pos = None
    su_master_pos = None
    
    for r in range(5):
        for c in range(5):
            piece = state.board.grid[r][c]
            # Buscamos al Maestro (Asumimos que la clase Piece tiene el atributo is_master)
            if piece is not None and getattr(piece, 'is_master', False):
                if piece.color == player:
                    mi_master_pos = (r, c)
                elif piece.color == opponent:
                    su_master_pos = (r, c)
                    
    score = 0
    # Premia estar cerca del templo enemigo (usando distancia Manhattan)
    if mi_master_pos:
        dist_mia = abs(mi_master_pos[0] - templo_enemigo[0]) + abs(mi_master_pos[1] - templo_enemigo[1])
        score += (10 - dist_mia) * 2 
        
    if su_master_pos:
        dist_suya = abs(su_master_pos[0] - mi_templo[0]) + abs(su_master_pos[1] - mi_templo[1])
        score -= (10 - dist_suya) * 2
        
    return score

# 4) Ventaja material (piezas restantes)
def piezas_restantes(state, player):
    opponent = 'BLUE' if player == 'RED' else 'RED'
    player_pieces = 0
    opponent_pieces = 0
    
    for row in state.board.grid:
        for piece in row:
            if piece is not None:
                if piece.color == player:
                    player_pieces += 1
                elif piece.color == opponent:
                    opponent_pieces += 1
                    
    return (player_pieces - opponent_pieces) * 3

# 5) Amenazas de captura inmediatas
def amenaza_captura(state, player):
    opponent = 'BLUE' if player == 'RED' else 'RED'
    mis_amenazas = 0
    sus_amenazas = 0
    
    # Revisar si mis movimientos caen sobre una pieza enemiga
    for move in state.get_all_legal_moves(player):
        destino = state.board.grid[move.end[0]][move.end[1]]
        if destino is not None and destino.color == opponent:
            mis_amenazas += 1
            
    # Revisar si sus movimientos caen sobre mis piezas
    for move in state.get_all_legal_moves(opponent):
        destino = state.board.grid[move.end[0]][move.end[1]]
        if destino is not None and destino.color == player:
            sus_amenazas += 1
            
    return mis_amenazas - sus_amenazas

# [cite_start]Registro de heurísticas disponibles [cite: 24]
HEURISTICS = {
    "centro": control_centro,
    "movilidad": movilidad,
    "templo": distancia_templo,
    "piezas": piezas_restantes,
    "amenaza": amenaza_captura
}

# FUNCIÓN DE EVALUACIÓN CONFIGURABLE
class Evaluador:
    def __init__(self, activas=None, pesos=None):
        if activas is None:
            activas = list(HEURISTICS.keys())

        self.funciones = [HEURISTICS[nombre] for nombre in activas]

        if pesos is None:
            pesos = [1.0] * len(self.funciones)

        self.pesos = pesos

    def __call__(self, state, player):
        # Corrección vital: 'winner' es atributo en tu código, no función
        ganador = state.winner
        opponent = 'BLUE' if player == 'RED' else 'RED'

        if ganador == player:
            return 100000
        if ganador == opponent:
            return -100000

        valor = 0
        for f, w in zip(self.funciones, self.pesos):
            valor += w * f(state, player)

        return valor