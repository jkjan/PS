import sys


def solution(n, path, order):
    sys.setrecursionlimit(1000000)
    graph = make_graph(n, path)
    before, after = make_keys(n, order)

    if before[0] != 0:
        return False

    visited = [False for _ in range(n)]
    visited[0] = True
    unavailable = set()
    dfs(0, visited, before, after, graph, unavailable)

    return all(x for x in visited)


def make_keys(n, order):
    before = [i for i in range(n)]
    after = [i for i in range(n)]

    for [A, B] in order:
        before[B] = A
        after[A] = B

    return before, after


def make_graph(n, path):
    graph = [[] for _ in range(n)]
    for [from_, _to] in path:
        graph[from_].append(_to)
        graph[_to].append(from_)
    return graph


def dfs(node, visited, before, after, graph, unavailable):
    before[after[node]] = after[node]

    if after[node] != node and after[node] in unavailable:
        unavailable.remove(after[node])
        visited[after[node]] = True
        dfs(after[node], visited, before, after, graph, unavailable)

    for adj in graph[node]:
        if not visited[adj]:
            if before[adj] != adj:
                unavailable.add(adj)
            else:
                visited[adj] = True
                dfs(adj, visited, before, after, graph, unavailable)


n = 9
path = [[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]]
order = [[1, 0]]

print(solution(n, path, order))