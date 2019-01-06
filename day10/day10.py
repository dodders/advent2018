from itertools import count


# parse points into (x, y, vx, vy) tuples
def get_line(line):
    obracket1 = line.find('<')
    comma1 = line.find(',')
    clbracket1 = line.find('>')
    obracket2 = line.find('<', clbracket1)
    comma2 = line.find(',', obracket2)
    clbracket2 = line.find('>', comma2)
    return tuple(map(int, [line[obracket1 + 1:comma1], line[comma1 + 1:clbracket1],
                     line[obracket2 + 1:comma2], line[comma2 + 1:clbracket2]]))


def get_bounds(points):
    maxx = max(points, key=lambda x: x[0])[0]
    minx = min(points, key=lambda x: x[0])[0]
    maxy = max(points, key=lambda x: x[1])[1]
    miny = min(points, key=lambda x: x[1])[1]
    return minx, maxx, miny, maxy


def get_area(points):
    minx, maxx, miny, maxy = get_bounds(points)
    return (maxx - minx + 1) * (maxy - miny + 1)


def get_min_area(points):
    prev = get_area(points)
    for i in count():
        points = move(points, 1)
        area = get_area(points)
        if area > prev:
            return i
        else:
            prev = area


def gprint(points):
    minx, maxx, miny, maxy = get_bounds(points)
    pts = [(x, y) for x, y, vx, vy in points]
    for y in range(miny, maxy + 3):
        for x in range(minx, maxx + 1):
            print('#' if (x, y) in pts else '.', end='')
        print()
    print('==============================')
    print(' ')


def move(points, t):
    return [(x + vx * t, y + vy * t, vx, vy) for x, y, vx, vy in points]


# with open('data10test.txt') as f:
with open('data10.txt') as f:
    lines = f.read().split('\n')

points = list(map(get_line, lines))
revs = get_min_area(points)
print('revolutions:', revs)
points = move(points, revs)
gprint(points)



