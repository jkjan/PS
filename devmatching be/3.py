def solution(n, edges, k, a, b):
    def get_graph():
        for P, Q in edges:
            graph[P].append(Q)
            graph[Q].append(P)

    def dfs(used, v, depth):
        if depth <= k and v == b:
            for x in used:
                total_used.add(x)
        if depth >= k:
            return False

        for adj in graph[v]:
            if not visited[adj]:
                used.add((v, adj))
                visited[adj] = True
                dfs(used, adj, depth + 1)
                visited[adj] = False
                used.remove((v, adj))

    graph = [[] for _ in range(n)]
    visited = [False for _ in range(n)]
    total_used = set()
    visited[a] = True

    get_graph()
    dfs(set(), a, 0)

    answer = 0
    dup = 0
    for p, q in total_used:
        if (q, p) not in total_used:
            answer += 1
        else:
            dup += 1

    answer += dup // 2
    return answer


n = 8
edges = [[0,1],[1,2],[2,3],[4,0],[5,1],[6,1],[7,2],[7,3],[4,5],[5,6],[6,7]]
k = 4
a = 0
b = 3
print(solution(n, edges, k, a, b))