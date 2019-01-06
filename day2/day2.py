with open('input2.txt') as f:
    data = f.readlines()


def part1():
    two = 0
    three = 0

    for d in data:
        charcount = {}
        for c in d:
            if c not in charcount:
                charcount[c] = 1
            else:
                charcount[c] = charcount[c] + 1
        if 2 in charcount.values():
            two = two + 1
        if 3 in charcount.values():
            three = three + 1

    print('checksum is ', two, ' x ', three, ' = ', two * three)


def diffstr(s1, s2):
    ct = 0
    diff = 0
    ret = ''
    for c in s1:
        if c == s2[ct]:
            ret = ret + c
        else:
            diff = diff + 1
        ct = ct + 1
    if diff == 1:
        return ret
    else:
        return None


def part2():
    data2 = data.copy()
    for d1 in data:
        for d2 in data2:
            ret = diffstr(d1, d2)
            if ret is not None:
                print('match found:', d1, ' to ', d2, ' diff ', ret)


part2()
