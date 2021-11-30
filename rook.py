from piece import Piece, PieceException


class Rook(Piece):
    def get_moves(self):
        moves = []
        file = self.__pos[0]
        rank = self.__pos[1]

        for temp_rank in range(1, 9, 1):
            if temp_rank == rank:
                pass
            else:
                temp_move = [self.__pos[0], temp_rank]
                moves.append(temp_move)

        for temp_file in 'abcdefgh':
            if temp_file == file:
                pass
            else:
                temp_move = [temp_file, rank]
                moves.append(temp_move)

        return moves
