from piece import Piece, PieceException
from rook import Rook
from bishop import Bishop


class Queen(Piece):
    def get_moves(self):
        moves = []

        temp_rook = Rook(self.__pos, self.__colour)
        temp_bishop = Bishop(self.__pos, self.__colour)

        rook_moves = temp_rook.get_moves()
        bishop_moves = temp_bishop.get_moves()

        moves += rook_moves + bishop_moves
        return moves
