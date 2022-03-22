
def solution(n, edges):
    graph = [[] for _ in range(n)]
    edge_set = set()
    dfs_num = [0 for _ in range(n)]
    total = 0

    for ea, eb in edges:
        graph[ea].append(eb)
        graph[eb].append(ea)

    def dfs(v):
        nonlocal total

        for adj in graph[v]:
            if (v, adj) not in edge_set:
                total += dfs_num[v]
                v_origin = dfs_num[v]
                adj_origin = dfs_num[adj]

                edge_set.add((v, adj))
                dfs_num[v] = dfs_num[v] if (adj, v) not in edge_set else 0
                dfs_num[adj] = dfs_num[v] + 1

                dfs(adj)

                dfs_num[v] = v_origin
                dfs_num[adj] = adj_origin
                edge_set.remove((v, adj))

            else:
                if adj != v and dfs_num[adj] < dfs_num[v]:
                    total -= 1

    dfs(0)
    return total


# n = 4
# edges = [[2,3],[0,1],[1,2]]
# 8

n = 5
edges = [[0,1],[0,2],[1,3],[1,4]]
# 16

print(solution(n, edges))
