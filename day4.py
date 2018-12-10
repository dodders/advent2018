with open('gddata4sorted.txt') as f:
# with open('data4test.txt') as f:
    data = f.readlines()


def parse(s):
    r = {}
    endb = s.find(']')
    r['ts'] = s[1:endb]
    text = s[endb+1:].strip()
    r['text'] = text
    idhash = text.find('#')
    if text.startswith('Guard'):
        r['guardid'] = text[idhash+1:text.find(' ', idhash+1)]
        r['mode'] = 'begins'
    elif text.startswith('falls'):
        r['mode'] = 'falls'
    elif text.startswith('wakes'):
        r['mode'] = 'wakes'
    else:
        r['mode'] = 'unknown'
    return r


def getdate(ts):
    return ts[5:10]


def getmins(ts):
    return int(ts[14:16])


def totalsleep(guard):
    total = 0
    times = guard['times']
    for x in range(0, len(times), 2):
        total = total + getmins(times[x+1]) - getmins(times[x])
    return total


def getguardwithmaxsleep():
    guards = {}
    guard = None
    gwithmax = (None, 0)
    for line in data:
        g = parse(line)
        if g['mode'] == 'begins':
            if guard is not None:
                guard['total'] = totalsleep(guard)
                if guard['total'] > gwithmax[1]:
                    gwithmax = (guard['id'], guard['total'])
                guards[guard['id']] = guard
            if g['guardid'] in guards:
                guard = guards[g['guardid']]
            else:
                guard = {'id': g['guardid'], 'starts': [], 'times': []}
            guard['starts'].append(g['ts'])
        if g['mode'] == 'falls':
            guard['times'].append(g['ts'])
        if g['mode'] == 'wakes':
            guard['times'].append(g['ts'])
    print('all guards:', guards)
    print('guard, total mins:', gwithmax)
    return guards[gwithmax[0]]


def findmin(g):
    mins = {}
    maxmins = (None, 0)
    times = guard['times']
    for x in range(0, len(times), 2):
        for y in range(getmins(times[x]), getmins(times[x+1])):
            if y in mins:
                mins[y] = mins[y] + 1
            else:
                mins[y] = 1
            if mins[y] > maxmins[1]:
                maxmins = (y, mins[y])
    return maxmins


guard = getguardwithmaxsleep()
minute = findmin(guard)
print('minute, total, guard:', minute[0], minute[1], guard)
print('answer =', minute[0], '*', int(guard['id']), '=', minute[0] * int(guard['id']))


