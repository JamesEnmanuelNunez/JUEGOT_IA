
from src.utils.constants import PIECE_MASTER, PIECE_STUDENT

class Piece:
    """
    Representa una pieza individual en el tablero de Onitama.
    """
    def __init__(self, color: str, kind: str):
        """
        :param color: 'RED' o 'BLUE' (definidos en constants.py)
        :param kind: 'M' (Maestro) o 'S' (Estudiante)
>>>>>>> merge-principal
        """
        self.color = color
        self.kind = kind

    def __str__(self) -> str:
        """Representación visual rápida: R_M, B_S, etc."""
        return f"{self.color[0]}_{self.kind[0]}"

    def __repr__(self) -> str:
        return self.__str__()

