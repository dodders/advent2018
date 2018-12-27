import sys
import collections as coll

# with open('data12test.txt') as f:
# with open('data12.txt') as f:
with open('data12mod.txt') as f:
    init = f.readline().replace('initial state: ', '').replace('\n', '')
    f.readline()
    rules = f.read().split('\n')

with open('day12result.txt') as f:
    res = list(map(lambda x: ''.join(x), f.read().split('\n')))


def compare(p, r):
    pstr = ''.join(p)
    return pstr[:pstr.rfind('#') + 1] == r[:r.rfind('#') + 1]


def get_pots(s):
    ret = coll.deque(s)
    ret.appendleft('.')
    ret.appendleft('.')
    ret.appendleft('.')
    ret.append('.')
    return ret, 3  # 3 is the zero pointer


def pprint(pots, gen):
    print('{:2d}: '.format(gen), end='')
    for p in pots:
        print(p, end='')
    print()


def apply(pots, rules, zptr):
    ret = coll.deque()
    lpots = len(pots)
    for i in range(lpots + 1):
        rule_found = False
        # find pots to match - pad with .s if they extend too far left or right.
        pot = ['', '', '', '', '']
        idx = 0
        for x in range(-2, 0):
            if i + x >= 0:
                pot[idx] = pots[i + x]
            else:
                pot[idx] = '.'
            idx += 1
        for x in range(0, 3):
            if i + x < lpots:
                pot[idx] = pots[i + x]
            else:
                pot[idx] = '.'
            idx += 1
        pot = ''.join(pot)
        # match against rules.
        if pot == '.....':
            ret.append('.')
        else:
            for r in rules:
                if r[:5] == pot:
                    ret.append(r[-1])
                    rule_found = True
                    break
            if not rule_found:
                if i < lpots:  # avoid too many trailing .s
                    ret.append('.')
    return ret, zptr


def sum_pot_nbrs(pots, zptr):
    s = 0
    for x in range(len(pots)):
        s = s + x - zptr if pots[x] == '#' else s
    return s

# print(init, rules)
limit = int(sys.argv[1])
print('running for', limit, 'generations...')
pots, zptr = get_pots(init)
for gen in range(0, limit + 1):
    (pots, zptr) = apply(pots, rules, zptr) if gen > 0 else (pots, zptr)
    if gen % 500 == 0 or gen == 20:
        s = sum_pot_nbrs(pots, zptr)
        print('sum', s, 'for gen', gen)
        # pprint(pots, gen)
        # if not compare(pots, res[gen]):
        #     print('error in line', gen)
        #     print('actual  ', ''.join(pots))
        #     print('expected', res[gen])
        #     break
# print()
# print('sum of pot nbrs:', s)  # part 1 answer = 1987

