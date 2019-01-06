import math as m


def get_cell_power(x, y, serial):
    rack = x + 10
    p = ((rack * y) + serial) * rack
    return int(str(m.trunc(p / 100))[-1]) - 5


def test_cell_power():
    print(get_cell_power(3, 5, 8), 4)
    print(get_cell_power(122, 79, 57), -5)
    print(get_cell_power(217, 196, 39), 0)
    print(get_cell_power(101, 153, 71), 4)


def get_grid(size, serial):
    grid = {}
    for y in range(1, size + 1):
        for x in range(1, size + 1):
            grid[(x, y)] = get_cell_power(x, y, serial)
    return grid


def get_totals(grid, x, y, dial):
    tot = 0
    for iy in range(y, y + dial):
        for ix in range(x, x + dial):
            tot += grid[(ix, iy)]
    return tot


def print_grid(grid, size):
    for y in range(1, size + 1):
        for x in range(1, size + 1):
            print('{:4d}'.format(grid[(x, y)]), end='')
        print()
    print()


def print_square(grid, x, y, dial):
    for iy in range(y, y + dial):
        for ix in range(x, x + dial):
            print('{:3d}'.format(grid[(ix, iy)]), end='')
        print()


def summed_area(grid, size):
    ret = {}
    for y in range(1, size + 1):
        for x in range(1, size + 1):
            s = grid[(x, y)] if (x, y) in grid else 0
            s = s + ret[(x - 1, y)] if (x - 1, y) in ret else s
            s = s + ret[(x, y - 1)] if (x, y - 1) in ret else s
            s = s - ret[(x - 1, y - 1)] if (x - 1, y - 1) in ret else s
            ret[(x, y)] = s
    return ret


# get sum of area starting at x, y with size dial
def get_area(sgrid, x, y, dial):
    a = sgrid[x - 1, y - 1] if (x - 1, y - 1) in sgrid else 0
    b = sgrid[x + dial - 1, y - 1] if (x + dial - 1, y - 1) in sgrid else 0
    c = sgrid[x - 1, y + dial - 1] if (x - 1, y + dial - 1) in sgrid else 0
    d = sgrid[x + dial - 1, y + dial - 1] if (x + dial - 1, y + dial - 1) in sgrid else 0
    # print('d', d, 'a', a, 'b', b, 'c', c)
    return d + a - b - c


def get_max_total(sgrid, size, dial):
    mtot = -10000
    mpoint = ()
    for y in range(1, size - dial - 1):
        for x in range(1, size - dial - 1):
            tot = get_area(sgrid, x, y, dial)
            # print('dial', dial, 'total', tot, ' at point', x, y)
            if tot > mtot:
                mtot = tot
                mpoint = (x, y)
    return mtot, mpoint


def get_max_overall(sgrid, size):
    otot = 0
    odial = 0
    opoint = ()
    for dial in range(1, size + 1):
        if dial % 10 == 0:
            print('doing dial', dial)
        tot, point = get_max_total(sgrid, size, dial)
        # print('dial', dial, 'total', tot, ' at point', point)
        if tot > otot:
            otot = tot
            opoint = point
            odial = dial
    return otot, opoint, odial


# # part 1 answer is 21, 13 with size 28.
size = 300
serial = 9110
raw_grid = get_grid(size, serial)
# print_grid(grid, size)
# print('total:', get_totals(grid, 90, 269, 16), '\n')
sgrid = summed_area(raw_grid, size)
print('point total:', get_area(sgrid, 90, 269, 16))
print('max total:', get_max_total(sgrid, size, 16))
print('overall total, point, dial:', get_max_overall(sgrid, size))
# tot, point, dial = get_max_overall(sgrid, size)
# print('total', tot, 'at point', point, 'with dial', dial)
