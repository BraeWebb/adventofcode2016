class KeyPad(object):
    def __init__(self):
        self.location = [0, 0]
        self.directions = {'U': (1, 0), 'D': (-1, 0), 'L': (0, -1), 'R': (0, 1)}

    def move(self, moves):
        for move in moves:
            loc = [self.location[0] + self.directions[move][0], self.location[1] + self.directions[move][1]]
            self.location = loc if self.in_bounds(loc) else self.location
        return self.get_location()

    def in_bounds(self, location):
        return max(abs(location[0]), abs(location[1])) <= 1

    def get_location(self):
        return ((self.location[0] +2)*6) % 9 + self.location[1] + 2

class AdvancedKeyPad(KeyPad):
    def __init__(self):
        super().__init__()
        self.location = [0, -2]

    def in_bounds(self, location):
        return (abs(location[0]) + abs(location[1])) <= 2

    def get_location(self):
        if self.location[0] == -2:
            return 'D'
        if self.location[0] == 2:
            return 1
        # magic
        return hex(((self.location[0] -1)*9) % 13 + self.location[1] + 3)[2:]

def getCode(moves, keypadClass):
    keypad = keypadClass()
    return ''.join([str(keypad.move(row)) for row in moves]).upper()

with open('inputs.txt') as f:
    moves = f.read().splitlines()
    code = getCode(moves, KeyPad)
    print(code)
    advanced = getCode(moves, AdvancedKeyPad)
    print(advanced)
