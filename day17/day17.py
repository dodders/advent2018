with open('test.txt') as f:
    data = f.read().split('\n')


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
    for y in range(miny - 1, maxy + 2):
        row = ''
        for x in range(minx - 1, maxx + 2):
            if (x, y) in water:
                row += '~'
            elif (x, y) == well:
                row += '+'
            elif (x, y) in clay:
                row += '#'
            else:
                row += '.'
        print(row)


def water_drop(drop):
    # move drop down unti it hits clay or water
    new_drop = (drop[0], drop[1] + 1)
    while new_drop not in clay and new_drop not in water:
        drop = new_drop
        new_drop = (drop[0], drop[1] + 1)
    water.append(drop)


coords = [getxy(d) for d in data]
clay = expand(coords)
water = []
maxx = max([c[0] for c in clay])
minx = min([c[0] for c in clay])
maxy = max([c[1] for c in clay])
miny = min([c[1] for c in clay])
well = (500, 0)
pprint()
for i in range(1, 6):
    print('water drop', i)
    water_drop((well[0], well[1]))
    pprint()
