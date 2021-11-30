from piece import Piece, PieceException


class Knight(Piece):
    def get_moves(self):
        moves = []
        file_index = 'abcdefgh'.index(self.__pos[0])
        rank_index = self.__pos[1]

        for i in range(-2, 3, 1):
            if i == 0:
                pass
            elif i == -2:
                if file_index-2 < 0:
                    pass
                else:
                    if rank_index+1 > 8:
                        pass
                    else:
                        temp_move = ['abcdefgh'[file_index-2], rank_index+1]
                        moves.append(temp_move)

                    if rank_index-1 < 1:
                        pass
                    else:
                        temp_move = ['abcdefgh'[file_index-2], rank_index-1]
                        moves.append(temp_move)
            elif i == -1:
                if file_index-1 < 0:
                    pass
                else:
                    if rank_index+2 > 8:
                        pass
                    else:
                        temp_move = ['abcdefgh'[file_index-1], rank_index+2]
                        moves.append(temp_move)

                    if rank_index-2 < 1:
                        pass
                    else:
                        temp_move = ['abcdefgh'[file_index-1], rank_index-2]
                        moves.append(temp_move)
            elif i == 1:
                if file_index+1 > 7:
                    pass
                else:
                    if rank_index+2 > 8:
                        pass
                    else:
                        temp_move = ['abcdefgh'[file_index+1], rank_index+2]
                        moves.append(temp_move)

                    if rank_index-2 < 1:
                        pass
                    else:
                        temp_move = ['abcdefgh'[file_index+1], rank_index-2]
            elif i == 2:
                if file_index+2 > 7:
                    pass
                else:
                    if rank_index+1 > 8:
                        pass
                    else:
                        temp_move = ['abcdefgh'[file_index+2], rank_index+1]
                        moves.append(temp_move)

                    if rank_index-1 < 1:
                        pass
                    else:
                        temp_move = ['abcdefgh'[file_index+2], rank_index-1]
                        moves.append(temp_move)

            return moves
