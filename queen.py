class QueenException(Exception):
    def __init__(self, message):
        self.message = message


class Queen:
    __pos = []
    __colour = ''

    def __init__(self, pos, colour):
        # Checking for valid position
        if pos[0] not in 'abcdefgh' or pos[1] < 1 or pos[1] > 8:
            raise QueenException('Invalid position')
        elif colour != 'white' and colour != 'black':
            raise QueenException('Invalid colour')

        # Setting the values provided
        self.__pos = pos
        self.__colour = colour

    def get_pos(self):
        return self.__pos

    def get_colour(self):
        return self.__colour

