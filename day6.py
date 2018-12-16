import numpy as np
import sys as s

np.set_printoptions(threshold=np.inf)
s.setrecursionlimit(10000)


def convert(lines):
    ret = []
    c = 65
    for l in lines:
        s = l.split()
        ret.append((int(s[0].strip().replace(',', '')), int(s[1].strip()), chr(c)))
        c += 1
    return ret


def get_axes(pad):
    maxx = max(points, key=lambda x: x[0])[0]
    maxy = max(points, key=lambda x: x[1])[1]
    return maxx + pad, maxy + pad


def load_points():
    for p in points:
        a[p[1], p[0]] = p[2]


def get_dist(x, y, p):
    return abs(x-p[0]) + abs(y-p[1])


def get_closest(dists):
    min_dist = min(dists, key=lambda x: x[1])
    ret = []
    for d in dists:
        if d[1] == min_dist[1]:
            ret.append(d[0])
    return ret


def calc_distances():
    for y in range(maxy):
        for x in range(maxx):
            print('doing distances for ', y, x)
            if a[y, x] == '.':
                distances = []
                for p in points:
                    dist = get_dist(x, y, p)
                    distances.append((p[2], dist))
                closest = get_closest(distances)
                if len(closest) == 1:
                    a[y, x] = closest[0]


def flood_fill(x, y, target, seen, in_area):
    # print(x, y, 'entered with ct', ct)
    if (x, y) in seen:  # node already processed.
        return True
    seen.append((x, y))
    if x < 0 or y < 0 or x == maxx or y == maxx:  # out of bounds.
        return False  # hit an edge!
    if a[y, x] != target:  # not part of the target.
        return True
    in_area.append((x, y))
    # keep going until we run out of nodes or hit an edge
    if flood_fill(x, y-1, target, seen, in_area):
        if flood_fill(x, y+1, target, seen, in_area):
            if flood_fill(x+1, y, target, seen, in_area):
                if flood_fill(x-1, y, target, seen, in_area):
                    return True
    return False


def get_areas():
    areas = []
    for p in points:
        # for y in range(maxy):
        #     for x in range(maxx):
        x = p[0]
        y = p[1]
        print('doing areas for', x, y)
        in_area = []
        if flood_fill(x, y, a[y, x], [], in_area):  # returns true if it doesn't hit an edge
            area = (a[y, x], len(in_area))
            if area not in areas:
                areas.append(area)
    print(areas)
    print(max(areas, key=lambda x: x[1]))


# with open('data6test.txt') as f:
with open('data6.txt') as f:
    lines = f.read().split('\n')

pad = 3
points = convert(lines)
print(points)
maxx, maxy = get_axes(pad)
a = np.full((maxy, maxx), '.', dtype=object)
load_points()
print('calculating distances...')
calc_distances()
print(a)
print('getting areas...')
get_areas()
# ar = []
# flood_fill(7, 0, 'C', [], ar)
# print(len(ar), ar)
