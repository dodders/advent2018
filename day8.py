def get_node(input):  # return [child_ct, meta_ct, meta, [children]]
    child_ct = int(input[0])
    meta_ct = int(input[1])
    if child_ct == 0:
        meta = input[2:2 + meta_ct]
        new_nodes = input[meta_ct + 2:]
        return new_nodes, [child_ct, meta_ct, meta_to_int(meta), []]
    else:
        children = []
        new_nodes2 = list(input[2:])
        for _ in range(child_ct):
            new_nodes2, child_nodes = get_node(new_nodes2)
            children.append(child_nodes)
        meta = new_nodes2[:meta_ct]
        node = [child_ct, meta_ct, meta_to_int(meta), children]
        return new_nodes2[meta_ct:], node


def meta_to_int(meta_list):
    return list(map(lambda x: int(x), meta_list))


def get_meta(node, ret):
    if len(nodes) == 0:
        return []
    ret.append(node[2])
    for child in node[3]:
        get_meta(child, ret)
    return ret


def sum_meta(lnodes):
    if len(lnodes) == 0:
        return 0
    s = sum(lnodes[2])
    for child in lnodes[3]:
        s = s + sum_meta(child)
    return s


def get_node_value(n):
    print('starting node:', n)
    if n[0] == 0:  # no child entries, value = sum of metadata
        print('node n zero children, sum', sum(n[2]), n)
        return sum(n[2])
    # if node has children, value is the sum of the values of the nodes pointed to by each metadata item.
    s = 0
    for ptr in n[2]:
        if ptr - 1 < len(n[3]):  # if referenced child doesn't exist, value is zero so don't need to explicitly handle
            v = get_node_value(n[3][ptr - 1])
            print('value for child', ptr, 'is', v, 'for node', n)
            s = s + v
            print('sum is', s)
    print('returning', s, 'for node', n)
    return s


# with open('data8test.txt') as f:
with open('data8.txt') as f:
    lines = f.read().replace('\n', '').split(' ')

# print(lines)
nlist, nodes = get_node(lines)
# print(nodes)
# t = [1, 7, [2, 1, 1, 1, 2, 2, 2], [[0, 11, [6, 2, 4, 8, 9, 3, 2, 8, 8, 1, 8], []]]]
# print('value of root node:', get_node_value(t))
print('value of root node:', get_node_value(nodes))
# part 1
# print(sum_meta(nodes))
# s = get_meta(nodes, [])
# print(s)
# flat = [item for sublist in s for item in sublist]
# print(flat)
# print(sum(flat))