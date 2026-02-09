

def draw_board(matrix):
    """
    Dibuja el tablero de Onitama.
    M = Maestro (Rojo), E = Estudiante (Rojo)
    m = Maestro (Azul), e = Estudiante (Azul)
    """
    print("\n      0     1     2     3     4")
    print("   " + "o-----" * 5 + "o")
    
    for r, row in enumerate(matrix):
       
        row_str = f" {r} |"
        for c, cell in enumerate(row):
            if cell == '.':
                display_char = "  .  " # Espacio vacío
            elif cell.isupper():
                display_char = f"  {cell}* " # Equipo Rojo con un brillo
            else:
                display_char = f" ({cell}) " # Equipo Azul entre paréntesis
            row_str += f"{display_char}|"
        
        print(row_str)
        print("   " + "o-----" * 5 + "o")

def draw_card(name, moves):
    """Dibuja la vista previa de una carta de movimiento"""
    print(f"\n>>> PERGAMINO DE MOVIMIENTO: {name.upper()} <<<")
    

if __name__ == "__main__":
    
    tablero_falso = [
        ['E', 'E', 'M', 'E', 'E'],
        ['.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.'],
        ['e', 'e', 'm', 'e', 'e']
    ]
    draw_board(tablero_falso)

    def draw_card_map(name, moves):
    """Dibuja un mapa visual de 5x5 para la carta"""
    print(f"\nMAPA DE MOVIMIENTO: {name}")
    grid = [["." for _ in range(5)] for _ in range(5)]
    center = 2
    grid[center][center] = "H" # Tu pieza (Home)
    
    for dx, dy in moves:
        # dx es fila (vertical), dy es columna (horizontal)
        # Invertimos dx para que 'negativo' sea hacia arriba
        grid[center + dx][center + dy] = "X"
        
    for row in grid:
        print("  " + " ".join(row))
    print(" (H=Pieza, X=Destino)")