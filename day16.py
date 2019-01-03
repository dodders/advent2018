with open('data16.1.txt') as f:
    data = f.read().split('\n')

d = [d for d in data if d != '']
print(d)
machine = []
for i in range(0, len(d), 3):
    before = [int(s) for s in d[i][9:19].split(',')]
    ops = [int(s) for s in d[i+1].split(' ')]
    after = [int(s) for s in d[i+2][9:19].split(',')]
    print('b', before, 'o', ops, 'a', after)
    machine.append((before, ops, after))
    

for state in machine:
    print(state)
