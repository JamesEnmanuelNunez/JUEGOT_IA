class Piece:
    def _init_(self, color: str, kind: str):
        """
        color: 'R' o 'B'
        kind: 'MAESTRO' o 'STUDIANTE'
        """
        self.color = color
        self.kind = kind

    def _str_(self):
        if self.color == "R":
            return "R" if self.kind == "MAESTRO" else "r"
        else:
            return "B" if self.kind == "MAESTRO" else "b"