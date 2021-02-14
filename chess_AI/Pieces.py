from abc import abstractmethod


class Piece:
    def __init__(self, color, position):
        self.file = position[0]
        self.rank = position[1]
        self.color = color

    @abstractmethod
    def legal_moves(self):
        pass


class Pawn(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)

    def legal_moves(self):
        pass


class Knight(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)

    def legal_moves(self):
        pass


class Bishop(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)

    def legal_moves(self):
        pass


class Rook(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)

    def legal_moves(self):
        pass


class Queen(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)

    def legal_moves(self):
        pass


class King(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)

    def legal_moves(self):
        pass
