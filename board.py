from pawn import Pawn
from bishop import Bishop
from knight import Knight
from rook import Rook
from queen import Queen
from king import King


class BoardException(Exception):
    def __init__(self, message):
        self.message = message


class Board:
    __board = []

    def __init__(self):
        for i in range(8):
            temp = []
            for j in range(8):
                temp.append(None)
            self.__board.append(temp)

        pieces = []

        for colour in ['white', 'black']:
            for file in 'abcdefgh':
                if colour == 'white':
                    pieces.append(Pawn([file, 2], colour))
                    if file in 'ah':
                        pieces.append(Rook([file, 1], colour))
                    elif file in 'bg':
                        pieces.append(Knight([file, 1], colour))
                    elif file in 'cf':
                        pieces.append(Bishop([file, 1], colour))
                    elif file == 'd':
                        pieces.append(Queen([file, 1], colour))
                    else:
                        pieces.append(King([file, 1], colour))
                else:
                    pieces.append(Pawn([file, 7], colour))
                    if file in 'ah':
                        pieces.append(Rook([file, 8], colour))
                    elif file in 'bg':
                        pieces.append(Knight([file, 8], colour))
                    elif file in 'cf':
                        pieces.append(Bishop([file, 8], colour))
                    elif file == 'd':
                        pieces.append(Queen([file, 8], colour))
                    else:
                        pieces.append(King([file, 8], colour))

        for piece in pieces:
            self.__add_piece(piece)

    def __add_piece(self, piece):
        pos = piece.get_pos()
        file = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'].index(pos[0])
        rank = pos[1] - 1

        self.__board[rank][file] = piece

    def display_command_line(self):
        for i in range(8):
            for j in range(8):
                piece = self.__board[i][j]
                if type(piece) == Pawn:
                    print('p', end=' ')
                elif type(piece) == Knight:
                    print('N', end=' ')
                elif type(piece) == Bishop:
                    print('B', end=' ')
                elif type(piece) == Rook:
                    print('R', end=' ')
                elif type(piece) == Queen:
                    print('Q', end=' ')
                elif type(piece) == King:
                    print('K', end=' ')
                else:
                    print('0', end=' ')
            print('\n', end='')
