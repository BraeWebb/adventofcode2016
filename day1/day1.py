class Grid(object):
    def __init__(self):
        self.location = [0,0]
        self.direction = 0
        self.directions = {0:(1,0), 1:(0,1), 2:(-1, 0), 3:(0, -1)}
        self.visited = []
        self.visit_count = {}

    def walk(self, code):
        if code[0] == 'R':
            self.direction = (self.direction + 1) % 4
        else:
            self.direction = (self.direction - 1) % 4

        steps = int(code[1:])
        direction = self.directions[self.direction]

        for i in range(steps):
            self.location[0] += direction[0]
            self.location[1] += direction[1]
            location = tuple(self.location)
            self.visited.append(location)
            if self.visit_count.get(location):
                self.visit_count[location] += 1
            else:
                self.visit_count[location] = 1

    def get_occurs(self, occurrence=1, visits=2):
        occurrences = 0
        for visit in self.visited:
            if self.visit_count[visit] == visits:
                if occurrences == occurrence:
                    return visit
                else:
                    occurrences += 1

    def get_blocks(self, location):
        return abs(location[0]) + abs(location[1])

    def get_location(self):
        return self.location


def walkPath(path):
    grid = Grid()
    for walk in path.split(', '):
        grid.walk(walk)
    return grid

def testPath(path):
    grid = walkPath(path)
    print('Finish Location: {}'.format(grid.get_location()))
    print('Blocks from Finish: {}'.format(grid.get_blocks(grid.get_location())))
    print('First Location Visited Twice: {}'.format(grid.get_occurs()))
    print('Blocks from First Location Visited Twice: {}'.format(grid.get_blocks(grid.get_occurs())))

#testPath('R2, L3')
#testPath('R2, R2, R2')
#testPath('R5, L5, R5, R3')

with open('inputs.txt') as f:
    path = f.readline()
    testPath(path)