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

opcodes = {11: eqri, 8: gtrr, 10: gtri, 14: eqir, 5: eqrr, 6: gtir, 1: banr,
           0: bani, 9: seti, 3: setr, 4: bori, 13: borr, 15: addr, 2: muli,
           12: addi, 7: mulr}
# opcodes = {}


# first answer 537 - correct!
def part2():
    with open('data16.2.txt') as f2:
        ops = f2.read().split('\n')
    regs = [0, 0, 0, 0]
    for op in ops:
        int_ops = [int(o) for o in op.split(' ')]
        func = opcodes[int_ops[0]]
        regs = func(regs, int_ops)
    print(regs)


def get_opcodes():
    print('cycling...')
    filtered_machine = [state for state in machine if state[1][0] not in opcodes.keys()]
    if len(filtered_machine) == 0:
        print('halting!')
        print(opcodes)
        exit()
    for state in machine:
        new_states = [(f.__name__, state[1][0], f(state[0], state[1])) for f in funcs]
        matches = [(f, o, news) for f, o, news in new_states if news == state[2]]
        matches = [(f, o, s) for f, o, s in matches if f not in opcodes.values()]
        # len 1 yields one match - eqri == opcode 11.
        # len 2 yields gtrr == 8
        if len(matches) == 1:
            opcode = matches[0][1]
            funcname = matches[0][0]
            if opcode in opcodes:
                if opcodes[opcode] != funcname:
                    print('conflict!', funcname, opcode, opcodes[opcode])
                    exit(1)
            else:
                opcodes[opcode] = funcname


# part 1 first guess 580 correct. i love list comprehensions.
def part1():
    ct = 0
    for state in machine:
        new_states = [f(state[0], state[1]) for f in funcs]
        matches = [s for s in new_states if s == state[2]]
        if len(matches) >= 3:
            print('matches', matches)
            ct += 1
    print('number of samples that behave like 3 or more opcodes', ct)


# part1()
# while True:
#     get_opcodes()  # just get opcodes.
part2()