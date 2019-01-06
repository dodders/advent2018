with open('input.txt') as f:
    data = f.readlines()

total = 0
for line in data:
    op = line[:1]
    amt = line[1:-1]
    if op == '+':
        total = total + amt
    else:
        total = total - amt

print('amt:', amt)
