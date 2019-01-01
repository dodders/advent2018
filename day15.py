import collections


def pprint(m):
    for c in m.values():
        print(c, end='')


def get_map(ls):
    m = collections.defaultdict()
    for y, l in enumerate(ls):
        for x, c in enumerate(l):
            m[(x, y)] = c
    return m


def grid_iter(g):
    for y in range(maxy):
        for x in range(maxx):
            yield (x, y), g[(x, y)]


def get_adjacent(point):
    ret = []
    ret.append((point[0] - 1, point[1])) if point[0] > 0 else None
    ret.append((point[0] + 1, point[1])) if point[0] < maxx else None
    ret.append((point[0], point[1] - 1)) if point[1] > 0 else None
    ret.append((point[0], point[1] + 1)) if point[1] < maxy else None
    return ret


def get_reachable(point):
    adj = get_adjacent(point)
    return [p for p in adj if grid[p] not in all_markers]


def get_routes(parent_point, pfrom, pto, weight, visited):  # a route is ((x1, y1), (x2, y2), weight)
    if pfrom in visited:
        return []
    # we have arrived so return this as a route
    if pfrom in get_reachable(pto):
        return [(parent_point, pto, weight + 1)]
    # expand search by next available squares
    visited.append(pfrom)
    routes = []
    for next_point in get_reachable(pfrom):
        if next_point not in visited:
            routes += get_routes(parent_point, next_point, pto, weight + 1, visited)
    return routes


def move(unit):
    targets = [t for t in units if t[1] != unit[1]]
    in_range = [get_reachable(t[0]) for t in targets]
    routes = []
    for target in in_range:
        routes += get_routes(unit[0], unit[0], target[0], 0, [])
    print('unit ', unit, 'targets', in_range)
    print('routes', routes)


with open('data15.1.txt') as f:
    lines = f.readlines()

unit_markers = ['E', 'G']
all_markers = ['E', 'G', '#']
grid = get_map(lines)
maxx = max(grid.keys(), key=lambda x: x[0])[0]
maxy = max(grid.keys(), key=lambda y: y[1])[1]
units = [(point, val, 3, 200) for point, val in grid_iter(grid) if val in unit_markers]
pprint(grid)
print(units)
for x in range(1):
    print('round %d' % x)
    for unit in units:
        # attack
        move(unit)
    pprint(grid)
    print(units)
