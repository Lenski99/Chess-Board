class KnightException(Exception):
    def __init__(self, message):
        self.message = message


class Knight:
    __pos = []
    __colour = ''

    def __init__(self, pos, colour):
        # Checking for valid position
        if pos[0] not in 'abcdefgh' or pos[1] < 1 or pos[1] > 8:
            raise KnightException('Invalid position')
        elif colour != 'white' and colour != 'black':
            raise KnightException('Invalid colour')

        # Setting the values provided
        self.__pos = pos
        self.__colour = colour

    def get_pos(self):
        return self.__pos

    def get_colour(self):
        return self.__colour

    def validate_move(self, move):
        file = move[1]
        rank = move[2]

        if file not in 'abcdefgh' or int(rank) < 1 or int(rank) > 8:
            return False

        file_diff = abs('abcdefgh'.index(self.__pos[0]) - 'abcdefgh'.index(file))
        rank_diff = abs(self.__pos[1] - int(rank))

        print(file_diff)
        print(rank_diff)

        if (file_diff == 1 and rank_diff == 2) or (file_diff == 2 and rank_diff == 1) and not (file_diff == 0 and rank_diff == 0):
            return True
        else:
            return False

    def make_move(self, move):
        self.__pos[0], self.__pos[1] = move[1], int(move[2])


