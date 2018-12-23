import math
import collections as coll


def get_players(ct):
    ret = {}
    for p in range(1, ct+1):
        ret[p] = 0
    return ret


def make(players, size):
    marbles = []
    player = 0
    cur = 0
    for m in range(0, size + 1):
        if m > 0 and m % 23 == 0:
            score = players[player]
            ptr = cur - 7
            # print('m div 23 found for marble', m, 'and player', player, 'at cur', cur, 'setting ptr to', ptr)
            if ptr < 0:  # wrap around
                ptr = len(marbles) - abs(ptr)
                # print('ptr wrapping from 0 to', cur)
            # print('player', player, 'score was', score, 'now adding marble', m, 'plus', marbles[ptr])
            score = score + m + marbles[ptr]
            players[player] = score
            del marbles[ptr]
            cur = ptr
        else:
            if len(marbles) <= 1:
                marbles.append(m)
                cur = m
            else:
                cur += 1
                if cur + 1 > len(marbles):  # wrap around
                    cur = 0
                marbles = marbles[:cur+1] + [m] + marbles[cur+1:]
                cur += 1
        # print('line', player, m, marbles)
        old_player = player
        player += 1
        if player > len(players):
            player = 1
    return marbles, old_player


def get_winner(players):
    top = max(players.values())
    for (p, s) in players.items():
        if s == top:
            return p, s


def part1(player_ct, size):
    print('--------------------------------------------------------------')
    print('running for players:', player_ct, 'and size', size)
    players = get_players(player_ct)
    marbs, p = make(players, size)
    # print('marbles', marbs)
    # print('players', players)
    print('high score (player, score):', get_winner(players))
    print('count of marbles', len(marbs), 'count should be', size - (math.trunc(size / 23) * 2) + 1)
    print('on player', p, 'and should be on player', size % player_ct)


def make2(players, size):
    # marbles = []
    marbles = coll.deque()
    player = 0
    # cur = 0
    for m in range(0, size + 1):
        if m > 0 and m % 10000 == 0:
            print('doing marble', m)
        if m > 0 and m % 23 == 0:
            score = players[player]
            # ptr = cur - 7
            # print('m div 23 found for marble', m, 'and player', player, 'at cur', cur, 'setting ptr to', ptr)
            # if ptr < 0:  # wrap around
            #     ptr = len(marbles) - abs(ptr)
                # print('ptr wrapping from 0 to', cur)
            # print('player', player, 'score was', score, 'now adding marble', m, 'plus', marbles[ptr])
            marbles.rotate(7)
            score = score + m + marbles[-1]
            players[player] = score
            # del marbles[ptr]
            # cur = ptr
            marbles.pop()
            marbles.rotate(-1)
        else:
            if len(marbles) <= 1:
                marbles.append(m)
                # cur = m
            else:
                # cur += 1
                # if cur + 1 > len(marbles):  # wrap around
                #     cur = 0
                # marbles = marbles[:cur+1] + [m] + marbles[cur+1:]
                marbles.rotate(-1)
                marbles.append(m)
                # cur += 1
        # print('line', player, m, marbles)
        old_player = player
        player += 1
        if player > len(players):
            player = 1
    return marbles, old_player


def part2(player_ct, size):
    print('--------------------------------------------------------------')
    print('running for players:', player_ct, 'and size', size)
    players = get_players(player_ct)
    marbs, p = make2(players, size)
    while marbs[-1] != 0:
        marbs.rotate()
    marbs.rotate()
    # print('marbles', marbs)
    # print('players', players)
    print('high score (player, score):', get_winner(players))
    print('count of marbles', len(marbs), 'count should be', size - (math.trunc(size / 23) * 2) + 1)
    print('on player', p, 'and should be on player', size % player_ct)


# part2(9, 25)
# part2(10, 1618)
# part2(13, 7999)
# part2(17, 1104)
# part2(21, 6111)
# part2(30, 5807)
# part2(462, 71938)  # answer is 398371
part2(462, 7193800)  # answer is