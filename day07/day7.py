import networkx as nx
import sys

sys.setrecursionlimit(10000)


def get_workers(ct):
    ret = {}
    for x in range(ct):
        ret[str(x)] = ''
    return ret


def get_runtime(step):
    # return ord(step) - 5  # for testing
    return ord(step) - 4  # for real


def get_graph(lines):
    g = nx.DiGraph()
    for l in lines:
        parent = l[5:6]
        child = l[36:37]
        g.add_node(parent, active=False)
        g.add_node(child, active=False)
        g.add_edge(parent, child)
    return g


def get_roots(g):
    cnodes = list(g.nodes)
    for e in g.edges:
        if e[1] in cnodes:
            cnodes.remove(e[1])
    return cnodes


def tick_tasks(todo, running, done):
    for item in list(running.items()):
        new_time = item[1] - 1
        if new_time > 0:  # not finished running
            running[item[0]] = new_time
        else:
            del running[item[0]]
            done.append(item[0])
            for node in g[item[0]]:
                if node not in done:
                    can_run = True
                    for pre in list(g.predecessors(node)):
                        if pre not in done:
                            can_run = False
                            break
                    if can_run:
                        todo.append(node)

# def part1(g, todo, done):  # this will start with roots.
#     if len(todo) == 0:
#         return done
#     todo.sort()
#     curr = todo[0]
#     print('done', done, 'todo', todo, 'doing', curr)
#     todo.remove(curr)
#     done.append(curr)
#     for node in g[curr]:
#         if node not in done:
#             can_run = True
#             for pre in list(g.predecessors(node)):
#                 if pre not in done:
#                     can_run = False
#                     break;
#             if can_run:
#                 todo.append(node)
#     return part1(g, todo, done)


#  sec = second, to do = list of available tasks, running = list of tuples of task & remaining task seconds,
#  done = list of completed tasks
def part2(sec, todo, running, done):
    if len(todo) == 0 and len(running) == 0:  # if no more nodes to process and no running tasks then stop
        return done
    tick_tasks(todo, running, done)
    todo.sort()
    for _ in range(worker_size - len(running)):  # if we have workers available, run available tasks
        # run next task.
        if len(todo) > 0:
            curr, curr_time = todo[0], get_runtime(todo[0])
            print('{0:10} {1:10} {2:10} {3:10}'.format(str(sec), curr, '.', ''.join(done)))
            todo.remove(curr)
            running[curr] = curr_time
    print('{0:10} {1:10} {2:10}'.format(str(sec), str(running), ''.join(done)))
    sec += 1
    return part2(sec, todo, running, done)


# with open('data7test.txt') as f:
with open('data7.txt') as f:
    lines = f.read().split('\n')
worker_size = 5
g = get_graph(lines)
roots = get_roots(g)
print('nodes', g.nodes)
print('edges', g.edges)
print('roots', roots)
# steps = part1(g, roots, [])
print('{0:10} {1:10} {2:10} '.format('Second', 'Running', 'Done'))
steps = part2(0, roots, {}, [])
print(steps)
for s in steps:
    print(s, end='')
print()