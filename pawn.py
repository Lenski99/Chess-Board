from piece import Piece, PieceException


class Pawn(Piece):
    __moved = False

    def get_moves(self):
        moves = []
        file = self.__pos[0]
        rank = self.__pos[1]

        # If white, increase rank
        if self.__colour == 'white':
            temp_move = [file, rank+1]
            moves.append(temp_move)

            if not self.__moved:
                temp_move = [file, rank+2]
                moves.append(temp_move)

        # If black, decrease rank
        else:
            temp_move = [file, rank-1]
            moves.append(temp_move)

            if not self.__moved:
                temp_move = [file, rank-2]
                moves.append(temp_move)

        return moves
