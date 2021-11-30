class PawnException(Exception):
    def __init__(self, message):
        self.message = message


class Pawn:
    __moved = False
    __pos = []
    __colour = ''

    def __init__(self, pos, colour):
        # Checking for valid position
        if pos[0] not in 'abcdefgh' or pos[1] < 1 or pos[1] > 8:
            raise PawnException('Invalid position')
        elif colour != 'white' and colour != 'black':
            raise PawnException('Invalid colour')

        # Setting the values provided
        self.__pos = pos
        self.__colour = colour

    def get_pos(self):
        return self.__pos

    def get_colour(self):
        return self.__colour

    def get_moved(self):
        return self.__moved


if __name__ == '__main__':
    try:
        Pawn(['t', 1], 'white')
    except PawnException as pe:
        print(pe.message)

    try:
        Pawn(['a', 0], 'white')
    except PawnException as pe:
        print(pe.message)

    try:
        Pawn(['a', 9], 'white')
    except PawnException as pe:
        print(pe.message)

    try:
        Pawn(['a', 2], 'blue')
    except PawnException as pe:
        print(pe.message)

    try:
        a = Pawn(['a', 2], 'white')
        print(a.get_pos())
        print(a.get_colour())
    except PawnException as pe:
        print(pe.message)
