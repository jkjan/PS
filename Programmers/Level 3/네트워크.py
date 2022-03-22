def solution(n, computers):
    visited = [False for _ in range(n)]

    def dfs(v):
        for adj in range(n):
            if computers[v][adj] and not visited[adj]:
                visited[adj] = True
                dfs(adj)

    answer = 0

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            answer += 1
            dfs(i)

    return answer
