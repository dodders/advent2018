def pprint(r, a, b):
    for x, recipie in enumerate(r):
        if x == a:
            print('(%s)' % recipie, end='')
        elif x == b:
            print('[%s]' % recipie, end='')
        else:
            print(' %s ' % recipie, end='')
    print()


def move(elf, score, max_size):
    pos = elf
    for _ in range(score + 1):
        pos += 1
        if pos >= max_size:
            pos = 0
    return pos


def find_in_list(find_str, l):
    for i in range(len(l) - len(find_str) + 1):
        comp = ''
        for ichar in l[i:i+len(find_str)]:
            comp += str(ichar)
        if find_str == comp:
            return i
    return None


after = 209231
# after = 59414
str_after = str(after)
# str_after = '01245'
init = [3, 7]
total_size = after + 10

recipies = init
e1 = 0  # elf pointers
e2 = 1
buf = ''.join(map(lambda x: str(x), init))
max_buf = len(str_after)

# for i in range(total_size):
i = 0
while True:
    i += 1
    new_recipie = recipies[e1] + recipies[e2]
    for s in str(new_recipie):
        recipies.append(int(s))
        buf += s
    if len(buf) > max_buf:
        buf = buf[-max_buf-20:]
    # pprint(recipies, e1, e2)
    # part 2 detection
    if str_after in buf:
        # buf += '0'
        # recipies.append(0)
        print('after %s found in buf %s in iteration %d' % (after, buf, i))
        print('total recipies %d and len of sequence is %d' % (len(recipies), len(str_after)))
        idx = find_in_list(str_after, recipies[-10:])
        print('last 10 of recipies %s with %s starting at %d.' % (recipies[-10:], str_after, idx))
        print('previous recipies is %d' % (len(recipies) - 10 + idx))
        # print(recipies)
        break
    e1 = move(e1, recipies[e1], len(recipies))
    e2 = move(e2, recipies[e2], len(recipies))
    # part 1 detection
    # if len(recipies) >= total_size:
    #     print('total recipies made!')
    #     print('next 10 after %2d are %s' % (after, recipies[after:total_size]))
    #     # part 1 answer after iteration 161216: 6126491027
    #     break

    # part 2
    # after 209231 found in buf 11691129129109617112092310 in iteration 15490908
    # total recipies 20191623 and len of sequence is 6
    # num of previous recipies is 20191617
    # last 10 of recipies [7, 1, 1, 2, 0, 9, 2, 3, 1, 0] with 209231 starting at 3.
    # previous recipies is 20191616
    # g2: 20191616 correct!
