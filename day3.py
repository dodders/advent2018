from operator import itemgetter


def parse(s):
    ret = {}
    at = s.find('@')
    comma = s.find(',')
    colon = s.find(':')
    times = s.find('x')
    ret['id'] = s[1:at].strip()
    ret['x'] = int(s[at+1:comma].strip()) + 1
    ret['y'] = int(s[comma+1:colon].strip()) + 1
    ret['xsize'] = int(s[colon+1:times].strip())
    ret['ysize'] = int(s[times+1:].strip())
    return ret


def insert(point, claimid):
    if point in points:
        idlist = points[point][1]
        idlist.append(claimid)
        points[point] = ('X', idlist)
    else:
        points[point] = (claimid, [claimid])


def pprint():
    # maxx = 0
    # maxy = 0
    # for p in points:
    #     if p[0] > maxx:
    #         maxx = p[0]
    #     if p[1] > maxy:
    #         maxy = p[1]
    maxx = max(points, key=itemgetter(0))[0] + 2
    maxy = max(points, key=itemgetter(1))[1] + 2
    for y in range(1, maxy):
        for x in range(1, maxx):
            p = (x, y)
            if p in points:
                print(points[p][0], end='')
            else:
                print('.', end='')
        print()


points = {}
claims = []
with open('data3.txt') as f:
    data = f.readlines()


for line in data:
    if line[:1] == '#':
        d = parse(line)
        claims.append(d['id'])
        for x in range(d['x'], d['x'] + d['xsize']):
            for y in range(d['y'], d['y'] + d['ysize']):
                insert((x, y), d['id'])


# print(points)
# pprint()
print(claims)
ct = 0
for v in points.values():
    if v[0] == 'X':
        ct = ct + 1
        for claim in v[1]:
            if claim in claims:
                claims.remove(claim)


print('overlaps = ', ct)
print(claims)

