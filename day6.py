import numpy as np


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
            # print('y, x:', y, x, 'row y', a[y])
            if a[y, x] == '.':
                distances = []
                for p in points:
                    dist = get_dist(x, y, p)
                    distances.append((p[2], dist))
                closest = get_closest(distances)
                if len(closest) == 1:
                    a[y, x] = closest[0].lower()


with open('data6test.txt') as f:
    lines = f.read().split('\n')

pad = 3
points = convert(lines)
maxx, maxy = get_axes(pad)
a = np.zeros((maxy, maxx), dtype=object)
a.fill('.')
load_points()
calc_distances()
print(a)

# a = np.zeros((2, 5))
# print(a)
# a[1, 3] = 1
# print(a[1])