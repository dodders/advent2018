def get_args(state, ops):
    s = state.copy()
    o, a, b, c = ops[0], int(ops[1]), int(ops[2]), int(ops[3])
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


def get_func(op):
    op_name = op[0]



opcodes = {11: eqri, 8: gtrr, 10: gtri, 14: eqir, 5: eqrr, 6: gtir, 1: banr,
           0: bani, 9: seti, 3: setr, 4: bori, 13: borr, 15: addr, 2: muli,
           12: addi, 7: mulr}

funcs = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]
with open('data.txt') as f:
    data = f.read().split('\n')


# part 1
def part1():
    ops = [d.split(' ') for d in data if d != '']
    state = [0, 0, 0, 0, 0, 0]
    # going to assume that the #ip op is the first op for now as it simplifies the part1 logic.
    reg_ptr = int(ops.pop(0)[1])  # set register pointer to the register referenced in the #ip operation.
    ptr = 0  # start with first instruction
    while len(ops) > ptr >= 0:
        state[reg_ptr] = ptr    # update register with current instruction ptr
        print('ip=%d %s ' % (ptr, state), end='')
        op = ops[ptr]
        func = [f for f in funcs if f.__name__ == op[0]][0]  # find function, should only be one.
        state = func(state, op)
        print('%s %s' % (op, state))
        ptr = state[reg_ptr]    # save instruction ptr
        ptr += 1  # inc ptr

    # part 1 halts so answer is in register 0.
    # correct answer is 2160.
    print('register 0:', state[0])


# part 1
def part2():
    print('starting...', flush=True)
    ops = [d.split(' ') for d in data if d != '']
    # going to assume that the #ip op is the first op for now as it simplifies the part1 logic.
    reg_ptr = int(ops.pop(0)[1])  # set register pointer to the register referenced in the #ip operation.
    # set intial state
    # ip=3 [0, 3, 1, 10551320, 10550400, 1] ['mulr', '5', '2', '4'] [0, 3, 1, 10551320, 1, 1]
    ptr = 0
    state = [1, 0, 0, 0, 0, 0]
    # ptr = 3
    # state = [0, 3, 1, limit, 10550400, 1]
    oldfirst = state[0]
    oldlast = state[5]
    while len(ops) > ptr >= 0:
        if ptr == 4:
            state[3] = 50
        state[reg_ptr] = ptr    # update register with current instruction ptr
        op = ops[ptr]
        func = [f for f in funcs if f.__name__ == op[0]][0]  # find function, should only be one.
        old_state = state
        state = func(state, op)
        # if oldfirst != state[0] or oldlast != state[5]:
        print('ip=%d %s %s %s ' % (ptr, old_state, op, state), flush=True)
            # oldfirst = state[0]
            # oldlast = state[5]
        ptr = state[reg_ptr]    # save instruction ptr
        ptr += 1  # inc ptr

    print('register 0: %d' % state[0])


# part1()
part2()
