with open('input.txt') as f:
    data = f.read().split('\n')

# data = [1, -2, 3, 1]

total = 0
freq = []
while True:
    for line in data:
        total = total + int(line)
        if total in freq:
            print('freq reached twice:', total)
            exit()
        else:
            freq.append(total)

# part 1 answer 547
# print('part 1 total:', total)

