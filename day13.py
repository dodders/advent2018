import collections
import operator


def get_maze(lines):
    m = {}
    for y, l in enumerate(lines):
        for x, char in enumerate(l):
            m[(x, y)] = char
    return m


def get_size(m):
    maxy = max(maze.keys(), key=lambda i: i[1])[1]
    maxx = max(maze.keys(), key=lambda i: i[0])[0]
    return maxx, maxy


def maze_iter(m):
    maxx, maxxy = get_size(m)
    for y in range(maxxy + 1):
        for x in range(maxx + 1):
            if (x, y) in m:
                yield(m[(x, y)]), (x, y)
            else:
                yield(' '), (x, y)


def pprint(carts, m):
    row = 0
    for c, point in maze_iter(m):
        if point[1] != row:
            row = point[1]
            print()
        print(c, end='') if point not in carts else print(reverse_directions[carts[point][0]], end='')
    print()


# return dictionary of carts (x, y) -> (direction, last intersection decision)
def find_carts(m):
    ret = m.copy()
    carts = {}
    for c, p in maze_iter(m):
        if c in replacements.keys():
            ret[p] = replacements[c]  # replace maze path under the cart
            # add cart with direction (x, y) -> (direction, turn buffer)
            carts[p] = (directions[c], turns.copy())
    return carts, ret


# tick moves each cart one step. logic:
# 1. move cart in it's current direction, regardless of the maze setting.
# 2. check for collisions. if no collisions then:
# 3. if cart is on a corner or an intersection, set new direction (e.g. 'rotating' the arrow.)
# also model the new direction logic in dictionaries rather than in code, just because.
def tick(cts, m):
    ret = {}
    left = cts.copy()
    for point, attribs in cts.items():
        if point not in crashed:  # if this cart has been crashed into already, then don't process it
            # move cart using the straights mappings.
            current_direction = attribs[0]
            turn_buffer = attribs[1]
            new_point = tuple(map(operator.add, point, straights[current_direction]))

            # check for a collision.
            if new_point in ret.keys() or new_point in cts.keys():
                print('crash at ', new_point)
                # return new_point, ret part 1 halted when a crash detected.
                # part 2, remove the 2 offending carts and carry on.
                if new_point in ret.keys():
                    del ret[new_point]
                if new_point in cts.keys():  # can't remove from cts as we are iterating over it, so store for later...
                    crashed.append(new_point)

            # continue processing if not crashed...
            else:
                # set new direction if the cart has hit a corner or an intersection (cart just rotates, doesn't move).
                instruction = m[new_point]
                if instruction == '-' or instruction == '|':  # same direction and turn buffer.
                    ret[new_point] = attribs

                elif instruction == '+':  # intersection
                    turn_buffer.rotate()  # get next left/straight/right turn from the rotation.
                    while compass[-1] != current_direction:  # rotate compass until it matches current direction
                        compass.rotate()
                    compass.rotate(rotation_amount[turn_buffer[-1]])  # rotate compass based on left/right/strait turn.
                    ret[new_point] = (compass[-1], turn_buffer)  # set new direction from compass.

                # corner logic is tricksy because the new direction depends on both the corner and the current direction...
                elif instruction == '\\' or instruction == '/':
                    corner = instruction + current_direction
                    ret[new_point] = (corners[corner], turn_buffer)  # look up new direction in the corners dictionary.

    return None, ret


# with open('data13.2test.txt') as f:
with open('data13.txt') as f:
    lines = f.read().split('\n')

# mappings for replacements, directions and turns.
replacements = {'^': '|', '>': '-', '<': '-', 'v': '|'}  # replacements for the maze sections under the initial carts.
directions = {'^': 'n', '>': 'e', '<': 'w', 'v': 's'}  # direction mappings for the intial carts.
reverse_directions = {'n': '^', 'e': '>', 'w': '<', 's': 'v'}  # reverse directions for pprint
turns = collections.deque(['s', 'l', 'r'])  # circular buffer for turn directions. COPY this into each point
compass = collections.deque(['n', 'e', 's', 'w'])  # rotating compass.
rotation_amount = {'l': 1, 'r': -1, 's': 0}  # amount of compass rotation for a l/r/s turn.
straights = {'e': (1, 0), 'w': (-1, 0), 'n': (0, -1), 's': (0, 1)}  # x, y adjustments for points on a straight
corners = {'/n': 'e', '/s': 'w', '/e': 'n', '/w': 's', '\\n': 'w', '\\s': 'e', '\\e': 's', '\\w': 'n', }  # corners

# actual work...
maze = get_maze(lines)
carts, maze = find_carts(maze)  # carts are (x, y) -> (direction, turn buffer, corner flag)
print('num carts', len(carts), 'carts', carts)
pprint(carts, maze)
ct = 0
while True:
    ct += 1
    print('cycle', ct)
    crash, carts = tick(carts, maze)
    if len(carts) == 1:
        print('only 1 cart left', carts)
        break
        # first guess 146,90
        # 2nd guess 145,90.
    print('num carts', len(carts), 'carts', carts)  # part 1 answer 94,78. first time, dammit!
    # pprint(carts, maze)
    print()

