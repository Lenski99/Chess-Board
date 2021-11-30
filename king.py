from piece import Piece, PieceException


class King(Piece):
    __in_check = False

    def get_moves(self):
        moves = []
        file_index = 'abcdefgh'.index(self.__pos[0])
        rank_index = self.__pos[1]

        # Check up and left
        if file_index-1 >= 0 and rank_index+1 <= 8:
            temp_move = ['abcdefgh'[file_index-1], rank_index+1]
            moves.append(temp_move)

        # Check up
        if rank_index+1 <= 8:
            temp_move = [self.__pos[0], rank_index+1]
            moves.append(temp_move)

        # Check up and right
        if file_index+1 <= 7 and rank_index+1 <= 8:
            temp_move = ['abcdefgh'[file_index+1], rank_index+1]
            moves.append(temp_move)

        # Check right
        if file_index+1 <= 7:
            temp_move = ['abcdefgh'[file_index+1], rank_index]
            moves.append(temp_move)

        # Check down and right
        if file_index+1 <= 7 and rank_index-1 >= 1:
            temp_move = ['abcdefgh'[file_index+1], rank_index-1]
            moves.append(temp_move)

        # Check down
        if rank_index-1 >= 1:
            temp_move = [self.__pos[0], rank_index-1]
            moves.append(temp_move)

        # Check down and left
        if file_index-1 >= 0 and rank_index-1 >= 1:
            temp_move = ['abcdefgh'[file_index-1], rank_index-1]
            moves.append(temp_move)

        # Check left
        if file_index-1 >= 0:
            temp_move = ['abcdefgh'[file_index-1], rank_index]
            moves.append(temp_move)

        return moves
