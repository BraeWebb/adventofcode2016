import sys

class Grid(object):
    def __init__(self, x, y):
        self.size = (x, y)
        self.pointer = [0, 0]
        self.grid = [['.' for x in range(x)] for y in range(y)]

    def _in_grid(self, x, y):
        return x >= 0 and y >= 0 and x < self.size[0] and y < self.size[1]

    def draw(self, x, y):
        for x_cord in range(self.pointer[0], x):
            for y_cord in range(self.pointer[1], y):
                if self._in_grid(x_cord, y_cord):
                    self.grid[y_cord][x_cord] = '#'

    def rotate_x(self, start, distance):
        new_col = [self.grid[i][start] for i in range(self.size[1])]
        new_col = new_col[-distance:] + new_col[:-distance]
        for i, value in enumerate(new_col):
            self.grid[i][start] = value

    def rotate_y(self, start, distance):
        self.grid[start] = self.grid[start][-distance:] + self.grid[start][:-distance]

    def print(self):
        for row in self.grid:
            print(''.join(row))

    def lit(self):
        count = 0
        for row in self.grid:
            count += row.count('#')
        return count


# grid = Grid(7, 3)
# grid.draw(3, 2)
# grid.rotate_x(1, 1)
# grid.rotate_y(0, 4)
# grid.rotate_x(1, 1)
# grid.print()

def run(stdin):
    grid = Grid(50, 6)
    for line in stdin.splitlines():
        if line[:4] == 'rect':
            grid.draw(*(int(x) for x in line[5:].split('x')))
        if line[:6] == 'rotate':
            y = int(line[line.index('=')+1:line.index('by')])
            by = int(line[line.index('by')+2:])
            grid.rotate_y(y, by) if line[7:10] == 'row' else grid.rotate_x(y, by)
    print(grid.lit())
    grid.print()

if __name__ == "__main__":
    run(sys.stdin.read())
