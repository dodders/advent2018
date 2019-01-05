def get_args(state, ops):
    s = state.copy()
    o, a, b, c = ops[0], ops[1], ops[2], ops[3]
    return s, o, a, b, c


def addr(state, ops):
    reg, o, a, b, c = get_args(state, ops)
    reg[c] = reg[a] + reg[b]
    return reg


def addi(state, ops):
    reg, o, a, b, c = get_args(state, ops)
    reg[c] = reg[a] + b
    return reg


def mulr(state, ops):
    reg, o, a, b, c = get_args(state, ops)
    reg[c] = reg[a] * reg[b]
    return reg


def muli(state, ops):
    reg, o, a, b, c = get_args(state, ops)
    reg[c] = reg[a] * b
    return reg


def banr(state, ops):
    reg, o, a, b, c = get_args(state, ops)
    reg[c] = reg[a] & reg[b]
    return reg


def bani(state, ops):
    reg, o, a, b, c = get_args(state, ops)
    reg[c] = reg[a] & b
    return reg


def borr(state, ops):
    reg, o, a, b, c = get_args(state, ops)
    reg[c] = reg[a] | reg[b]
    return reg


def bori(state, ops):
    reg, o, a, b, c = get_args(state, ops)
    reg[c] = reg[a] | b
    return reg


def setr(state, ops):  # copies reg a into reg c
    reg, o, a, b, c = get_args(state, ops)
    reg[c] = reg[a]
    return reg


def seti(state, ops):  # stores value a in reg c
    reg, o, a, b, c = get_args(state, ops)
    reg[c] = a
    return reg


def gtir(state, ops):  # value a > reg b
    reg, o, a, b, c = get_args(state, ops)
    if a > reg[b]:
        reg[c] = 1
    else:
        reg[c] = 0
    return reg


def gtri(state, ops):  # reg a > value b
    reg, o, a, b, c = get_args(state, ops)
    if reg[a] > b:
        reg[c] = 1
    else:
        reg[c] = 0
    return reg


def gtrr(state, ops):  # reg a > reg b
    reg, o, a, b, c = get_args(state, ops)
    if reg[a] > reg[b]:
        reg[c] = 1
    else:
        reg[c] = 0
    return reg


def eqir(state, ops):  # value a == reg b
    reg, o, a, b, c = get_args(state, ops)
    if a == reg[b]:
        reg[c] = 1
    else:
        reg[c] = 0
    return reg


def eqri(state, ops):  # reg a == value b
    reg, o, a, b, c = get_args(state, ops)
    if reg[a] == b:
        reg[c] = 1
    else:
        reg[c] = 0
    return reg


def eqrr(state, ops):  # reg a == reg b
    reg, o, a, b, c = get_args(state, ops)
    if reg[a] == reg[b]:
        reg[c] = 1
    else:
        reg[c] = 0
    return reg


# state = [[3, 2, 1, 1], [9, 2, 1, 2], [3, 2, 2, 1]]
# print('state', state)
funcs = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]
with open('data16.1.txt') as f:
    data = f.read().split('\n')

d = [d for d in data if d != '']
machine = []
for i in range(0, len(d), 3):
    before = [int(s) for s in d[i][9:19].split(',')]
    ops = [int(s) for s in d[i+1].split(' ')]
    after = [int(s) for s in d[i+2][9:19].split(',')]
    machine.append((before, ops, after))

ct = 0
for state in machine:
    new_states = [f(state[0], state[1]) for f in funcs]
    matches = [s for s in new_states if s == state[2]]
    if len(matches) >= 3:
        print('matches', matches)
        ct += 1
print('number of samples that behave like 3 or more opcodes', ct)

# part 1 first guess 580 correct. i love list comprehensions.
