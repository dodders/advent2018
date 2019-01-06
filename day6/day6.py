import numpy as np


def convert(lines):
    ret = []
    c = 65
    for l in lines:
        s = l.split(',')
        ret.append((int(s[0].strip()), int(s[1].strip()), chr(c)))
        c += 1
    return ret


def get_axes():
    maxx = max(points, key=lambda x: x[0])[0]
    maxy = max(points, key=lambda x: x[1])[1]
    return int(maxx) + 1, int(maxy) + 1


def load_points():
    for p in points:
        a[p[1], p[0]] = p[2]


def get_dist(x, y, p):
    return abs(x-p[0]) + abs(y-p[1])


def get_closest(dists):
    min_dist = min(dists, key=lambda x:x[1])
    ret = []
    for d in dists:
        if d[1] == min_dist[1]:
            ret.append(d[0])
    return ret


def calc_distances():
    for x in range(maxx):
        for y in range(maxy):
            if a[y, x] == '.':
                distances = []
                for p in points:
                    dist = get_dist(x, y, p)
                    distances.append((p[2], dist))
                a[y, x] = distances
                closest = get_closest(distances)
                if len(closest) == 1:
                    a[y, x] = closest[0].lower()
                else:
                    a[y, x] = '.'


with open('data6test.txt') as f:
    lines = f.read().split('\n')

points = convert(lines)
maxx, maxy = get_axes()
a = np.zeros((maxy+1, maxx+1), dtype=object)
a.fill('.')
load_points()
calc_distances()
print(a)
