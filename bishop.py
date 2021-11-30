from piece import Piece, PieceException


class Bishop(Piece):
    def get_moves(self):
        moves = []
        file_index = 'abcdefgh'.index(self.__pos[0])
        rank_index = self.__pos[1]

        # Checking up and right from current position
        for i in range(8):
            if i == 0:
                pass
            else:
                if file_index+i > 7 or rank_index+i > 8:
                    break
                else:
                    temp_move = ['abcdefgh'[file_index+i], rank_index+i]
                    moves.append(temp_move)

        # Checking down and right from current position
        for j in range(8):
            if j == 0:
                pass
            else:
                if file_index+j > 7 or rank_index-j < 1:
                    break
                else:
                    temp_move = ['abcdefgh'[file_index+j], rank_index-j]
                    moves.append(temp_move)

        # Checking down and left from current position
        for k in range(8):
            if k == 0:
                pass
            else:
                if file_index-k < 0 or rank_index-k < 1:
                    break
                else:
                    temp_move = ['abcdefgh'[file_index-k], rank_index-k]
                    moves.append(temp_move)

        # Checking up and left
        for l in range(8):
            if l == 0:
                pass
            else:
                if file_index-l < 0 or rank_index+l > 8:
                    break
                else:
                    temp_move = ['abcdefgh'[file_index-l], rank_index+l]
                    moves.append(temp_move)

        return moves
