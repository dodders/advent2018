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
    a = sgrid[x - 1 , y - 1]
    b = sgrid[x + dial - 1, y - 1]
    c = sgrid[x - 1, y + dial - 1]
    d = sgrid[x + dial - 1, y + dial - 1]
    print('d', d, 'a', a, 'b', b, 'c', c)
    return d + a - b - c


def get_max_total(grid, size, dial):
    mtot = 0
    mpoint = ()
    for y in range(1, size - dial - 1):
        for x in range(1, size - dial - 1):
            tot = get_totals(grid, x, y, dial)
            if tot > mtot:
                mtot = tot
                mpoint = (x, y)
    return mtot, mpoint


# # part 1 answer is 21, 13 with size 28.
size = 300
serial = 42
grid = get_grid(size, serial)
# print_grid(grid, size)
print('total:', get_totals(grid, 21, 61, 3), '\n')
sgrid = summed_area(grid, size)
print('summed total:', get_area(sgrid, 21, 61, 3))
