def get_forest(d):
    ret = {}
    for y, line in enumerate(d):
        for x, location in enumerate(line):
            ret[(x, y)] = location
    return ret


def pprint(f):
    maxx = max(f.keys(), key=lambda x: x[0])[0]
    maxy = max(f.keys(), key=lambda y: y[1])[1]
    for y in range(maxy + 1):
        row = ''
        for x in range(maxx + 1):
            row += f[(x, y)]
        print(row)


def get_adjacent(x, y, oldf):
    ret = []
    ret.append(oldf.get((x - 1, y - 1)))
    ret.append(oldf.get((x, y - 1)))
    ret.append(oldf.get((x + 1, y - 1)))
    ret.append(oldf.get((x - 1, y)))
    ret.append(oldf.get((x + 1, y)))
    ret.append(oldf.get((x - 1, y + 1)))
    ret.append(oldf.get((x, y + 1)))
    ret.append(oldf.get((x + 1, y + 1)))
    return [item for item in ret if item is not None]


def mutate(x, y, value, oldf):
    adj = get_adjacent(x, y, oldf)
    # open ground -> tree if has 3 or more adjacent trees
    if value == open_ground:
        if len([i for i in adj if i == tree]) >= 3:
            return tree
        return value
    # trees -> lumberyard if 3 or more adjacent acres are lumberyards
    elif value == tree:
        if len([i for i in adj if i == lumberyard]) >= 3:
            return lumberyard
        return value
    # lumberyard remains a lumberyard if adjacent to a tree and a lumberyard.
    elif value == lumberyard:
        if lumberyard in adj and tree in adj:
            return lumberyard
        return open_ground


def part1(oldf):
    for i in range(1, 11):
        newf = {}
        for p, v in oldf.items():
            newf[(p[0], p[1])] = mutate(p[0], p[1], v, oldf)
        print('minute', i)
        pprint(newf)
        print()
        oldf = newf
    wooded = len([x for x in oldf.values() if x == tree])
    lumbered = len([x for x in oldf.values() if x == lumberyard])
    # part1 answer wooded 1025 lumberyards 622 answer 637550 correct first time.
    print('wooded', wooded, 'lumberyards', lumbered, 'answer', wooded * lumbered)


def part2(oldf):
    # 1000000000 iterations
    for i in range(1, 1000000001):
        newf = {}
        for p, v in oldf.items():
            newf[(p[0], p[1])] = mutate(p[0], p[1], v, oldf)
        oldf = newf
        if i % 1000 == 0:
            print('answer for', i)
            wooded = len([x for x in oldf.values() if x == tree])
            lumbered = len([x for x in oldf.values() if x == lumberyard])
            # part2 answer
            print('wooded', wooded, 'lumberyards', lumbered, 'answer', wooded * lumbered)

    wooded = len([x for x in oldf.values() if x == tree])
    lumbered = len([x for x in oldf.values() if x == lumberyard])
    # part2 answer
    print('wooded', wooded, 'lumberyards', lumbered, 'answer', wooded * lumbered)
    # answers cycle through 7 numbers as per the part2out.txt file.
    # 1000000000 / 7 is even, so take the first number in the cycle: 201465.


with open('data.txt', 'r') as f:
    data = f.read().split('\n')
open_ground = '.'
tree = '|'
lumberyard = '#'
forest = get_forest(data)
pprint(forest)
part2(forest)
