def pprint(r, a, b):
    for x, recipie in enumerate(r):
        if x == a:
            print('(%s)' % recipie, end='')
        elif x == b:
            print('[%s]' % recipie, end='')
        else:
            print(' %s ' % recipie, end='')
    print()


# after = 209231
after = 59414
recipies = [3, 7]
str_after = str(after)
e1 = 0  # elf pointers
e2 = 1

i = 0
while True:
    i += 1
    new_recipie = recipies[e1] + recipies[e2]
    for s in str(new_recipie):
        recipies.append(int(s))
    # part 2 detection
    end = ''.join(map(str, recipies[-len(str_after):]))
    end_and_one = ''.join(map(str, recipies[-len(str_after)-1:-1]))
    if str_after == end or str_after == end_and_one:
        prev = len(recipies) - len(str_after)
        if str_after == end_and_one:
            prev -= prev
        print('%d found with %d previous recipies' % (after, prev))
        break
    # move elves
    e1 = (e1 + recipies[e1] + 1) % len(recipies)
    e2 = (e2 + recipies[e2] + 1) % len(recipies)
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
