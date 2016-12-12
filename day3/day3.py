def is_triangle(sides, verbose=False):
    possible = True
    for id, length in enumerate(sides):
        if verbose:
            print('Comparing side {} of length {} to {}'.format(id, length, sides[:id] + sides[id+1:]))
        if length >= sum(sides[:id] + sides[id+1:]):
            possible = False
    return possible

def to_int(str_list):
    return [int(i) for i in str_list]
#print(is_triangle([5, 10, 25], verbose=True))

with open('inputs.txt') as f:
    side_list = f.read().splitlines()
    triangles = 0
    for sides in side_list:
        sides = to_int(sides.split())
        if is_triangle(sides):
            triangles += 1
    print(triangles)


with open('inputs.txt') as f:
    sides = []
    lines = f.read().splitlines()
    for i in range(3):
        for line in lines:
            sides.append(line.split()[i])
    triangles = 0
    for triangle in [sides[i:i+3] for i in range(0, len(sides), 3)]:
        if is_triangle(to_int(triangle)):
            triangles += 1
    print(triangles)