from abc import abstractmethod


class Piece:
    def __init__(self):
        pass

    @abstractmethod
    def legal_moves(self):
        pass


class Pawn(Piece):
    def __init__(self):
        super().__init__()

    def legal_moves(self):
        pass


class Knight(Piece):
    def __init__(self):
        super().__init__()

    def legal_moves(self):
        pass


class Bishop(Piece):
    def __init__(self):
        super().__init__()

    def legal_moves(self):
        pass


class Rook(Piece):
    def __init__(self):
        super().__init__()

    def legal_moves(self):
        pass


class Queen(Piece):
    def __init__(self):
        super().__init__()

    def legal_moves(self):
        pass


class King(Piece):
    def __init__(self):
        super().__init__()

    def legal_moves(self):
        pass
