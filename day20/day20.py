# get first expression from string. expression is enclosed in ( and ) and may contain other expressions.
def get_expr(s):
    start = -1; ct = 0
    for i in enumerate(s):
        if i[1] == '(':
            if start == -1:
                start = i[0]
            ct += 1
        elif i[1] == ')':
            ct -= 1
        if ct == 0 and start > -1:  # found closing bracket
            return start, i[0]  # start and end positions
    return 0, 0


def parse(done, doing, curr):
    if len(doing) == 0:
        print(done, ' end')
    # if doing[0] == ')':
    #     print(done, '+', doing[0])
    #     return parse(done + doing[0], doing[1:], curr)
    elif doing[0] in ['N', 'S', 'E', 'W']:
        curr = do_move(doing[0], curr)
        # print(done, '+', doing[0])
        parse(done + doing[0], doing[1:], curr)
    elif doing[0] == '(':
        s, e = get_expr(doing)
        expr = doing[s+1:e]  # exclude the brackets
        opts = expr.split('|')
        for opt in opts:
            parse(done, opt + doing[e + 1:], curr)
        # parse(done + doing[0], doing[1:pos], curr) + parse(done + doing[0], doing[pos + 1:], curr)


def do_move(move, curr):
    curr = moves[move](curr)
    maze[curr] = doors[move]
    curr = moves[move](curr)
    maze[curr] = '.'  # room
    return curr


def pprint(m):
    minx = min(m, key=lambda x: x[0])[0]
    maxx = max(m, key=lambda x: x[0])[0]
    miny = min(m, key=lambda y: y[1])[1]
    maxy = max(m, key=lambda y: y[1])[1]
    for y in range(miny - 1, maxy + 2):
        row = ''
        for x in range(minx - 1, maxx + 2):
            row += m.get((x, y), '#')  # default to # for a wall if nothing else found
        print(row)


def west(point):
    return point[0] - 1, point[1]


def east(point):
    return point[0] + 1, point[1]


def north(point):
    return point[0], point[1] - 1


def south(point):
    return point[0], point[1] + 1


moves = {'W': west, 'E': east, 'S': south, 'N': north}
doors = {'W': '|', 'E': '|', 'S': '-', 'N': '-'}

with open('test1.txt') as f:
    ex = f.read()
rex = ex[1:-2]
maze = {(0, 0): 'X'}
# test1 = 'WNE'
# test1 = 'ENWWW(NEEE|SSE)W'
test1 = 'EN(NE|EN(S|W))W'
# test1 = 'ENWWW(NEEE|SSE(EE|N))'
# test1 = 'EN(NEWS|)SE(WNSE|)EE(SWEN|)NNN'
# test1 = 'ENNWSWW(NEWS|)SSSEEN(WNSE|)EE(SWEN|)NNN'
# test1 = 'ENNWSWW(NEWS|)SSSEEN'
# test1 = 'E(N|S|E|)W'
# test1 = 'ESSWWN(E|NNENN(EESS(WNSE|)SSS|WWWSSSSE(SW|NNNE)))'
# test1 = 'ES(E|)NE'
parse('', test1, (0, 0))  # done, route remaining, current point
print()
pprint(maze)
