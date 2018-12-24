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


def get_totals(grid, x, y):
    tot = 0
    for iy in range(y, y + 3):
        for ix in range(x, x + 3):
            tot += grid[(ix, iy)]
    return tot


def print_grid(grid):
    for y in range(1, size + 1):
        for x in range(1, size + 1):
            print('{:3d}'.format(grid[(x, y)]), end='')
        print()


def get_max_total(grid, size):
    mtot = 0
    mpoint = ()
    for y in range(1, size - 2):
        for x in range(1, size - 2):
            tot = get_totals(grid, x, y)
            if tot > mtot:
                mtot = tot
                mpoint = (x, y)
    return mtot, mpoint


size = 300
serial = 9110
grid = get_grid(size, serial)
print('total at point is', get_max_total(grid, size))

