with open('test.txt') as f:
    data = f.read().split('\n')


def get_max(s):
    if '..' not in s:
        return int(s)
    else:
        idx = s.find('..')
        return max(int(s[:idx]), int(s[idx+2:]))


def get_min(s):
    if '..' not in s:
        return int(s)
    else:
        idx = s.find('..')
        return min(int(s[:idx]), int(s[idx+2:]))


def getxy(s):
    xstr = s.find('x=')
    ystr = s.find('y=')
    comma = s.find(',')
    if s[0] == 'x':
        return s[2:comma], s[ystr+2:]
    else:
        return s[xstr+2:], s[2:comma]


def get_range(s):
    if '..' not in s:
        return int(s), int(s)
    else:
        idx = s.find('..')
        return int(s[:idx]), int(s[idx + 2:])


def expand(cs):
    ret = []
    for c in cs:
        xrange = get_range(c[0])
        yrange = get_range(c[1])
        for y in range(yrange[0], yrange[1] + 1):
            for x in range(xrange[0], xrange[1] + 1):
                ret.append((x, y))
    return ret


def pprint():
    for y in range(miny - 1, maxy + 1):
        row = ''
        for x in range(minx - 1, maxx + 1):
            if (x, y) in grid:
                row += '#'
            else:
                row += '.'
        print(row)


coords = [getxy(d) for d in data]
grid = expand(coords)
maxx = max([get_max(c[0]) for c in coords])
minx = min([get_min(c[0]) for c in coords])
maxy = max([get_max(c[1]) for c in coords])
miny = min([get_min(c[1]) for c in coords])
pprint()
