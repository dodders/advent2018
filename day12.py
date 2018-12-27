with open('data12test.txt') as f:
# with open('data12.txt') as f:
    init = f.readline().replace('initial state: ', '').replace('\n', '')
    f.readline()
    rules = f.read().split('\n')


def pprint(pots, gen):
    print('{:2d}: '.format(gen), end='')
    for p in pots:
        print(p, end='')
    print()


def apply(pots, rules):
    ret = ['.', '.']
    no_rules = []
    pots.append('.')
    for i in range(2, len(pots)):
        # print('doing', i - 2, 'pots are', pots[i-2:i+3])
        rule_found = False
        pot = pots[i-2:i+3]  # for debugging
        for r in rules:
            if r[:5] == ''.join(pots[i-2:i+3]):
                ret.append(r[-1])
                rule_found = True
                break
        if not rule_found:
            no_rules.append(i)
            ret.append('.')
    return ret, no_rules


# print(init, rules)
pots = list(init)
for _ in range(2):
    pots.insert(0, '.')
    pots.append('.')
pprint(pots, 0)
for gen in range(1, 21):
    pots, missing_rules = apply(pots, rules)
    pprint(pots, gen)
print()
# print('missing rules for', missing_rules)
