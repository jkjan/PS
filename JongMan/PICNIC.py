import sys


def solution():
    C = int(sys.stdin.readline().strip())
    for i in range(C):
        tc()


def get_input():
    n, _ = map(int, sys.stdin.readline().split())
    total = list(map(int, sys.stdin.readline().split()))
    tuples = []
    for i in range(len(total) - 1):
        if i % 2 == 0:
            tuples.append((total[i], total[i + 1]))
    return n, tuples


def tc():
    n, tuples = get_input()
    graph = make_graph(n, tuples)
    mated = [False for _ in range(n)]
    answer = mate(mated, graph)
    sys.stdout.write("%d\n" % answer)


def make_graph(n, tuples):
    graph = [[] for _ in range(n)]
    for a, b in tuples:
        graph[a].append(b)
        graph[b].append(a)
    return graph


def mate(mated, graph):
    now_mating = -1

    for i in range(len(graph)):
        if not mated[i]:
            now_mating = i
            break

    if now_mating == -1:
        return 1

    cnt = 0
    for friend in graph[now_mating]:
        if not mated[friend]:
            mated[now_mating] = mated[friend] = True
            cnt += mate(mated, graph)
            mated[now_mating] = mated[friend] = False

    return cnt


solution()