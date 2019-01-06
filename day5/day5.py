def comp(a, b):
    if a == b:
        return False
    if a.lower() == b or b.lower() == a:
        return True
    else:
        return False


def sprint(x):
    print(' ', end='')
    for c in chars[:100]:
        print(c, end='')
    print()
    print(x, end='')
    for i in range(0, x):
        print(' ', end='')
    print('^')


chars = []
# for letter in open("data5test.txt").read():
for letter in open("data5.txt").read():
    chars.append(letter)
print(len(chars))


x = 0
while True:
    try:
        # sprint(x)
        print(str(x) + ": " + chars[x] + chars[x+1])
        if comp(chars[x], chars[x+1]):
            print('Removed ' + chars[x] + chars[x+1])
            del chars[x+1]
            del chars[x]
            x = x - 2
            if x < 0:
                x = 0
        else:
            x += 1
    except IndexError:
        break


print('length:', len(chars))
