import heapq


def solution(grid, K):
    n = len(grid)
    dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    def get_cost(y, x):
        e_y, e_x = y + K - 1, x + K - 1
        return dp[e_y][e_x] - dp[e_y][x-1] - dp[y-1][e_x] + dp[y-1][x-1]

    def is_in(a, b, c, d):
        return (a <= c <= a + K - 1) and (b <= d <= b + K - 1)

    def is_over(a, b, c, d):
        return is_in(a, b, c + K - 1, d + K - 1) or is_in(a, b, c + K - 1, d) or is_in(a, b, c, d + K - 1) or is_in(a, b, c, d)

    for i in range(1, n+1):
        for j in range(1, n+1):
            dp[i][j] += (grid[i-1][j-1] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1])

    pq = []
    answer = 0
    for i in range(1, n - K + 2):
        for j in range(1, n - K + 2):
            cost = get_cost(i, j)
            heapq.heappush(pq, (-cost, i, j))

            backup = []
            while pq:
                max_can, ci, cj = heapq.heappop(pq)
                max_can *= -1
                heapq.heappush(backup, (-max_can, ci, cj))
                if not is_over(i, j, ci, cj):
                    answer = max(answer, max_can + cost)
                    break
            while backup:
                x = heapq.heappop(backup)
                heapq.heappush(pq, x)

    return answer


grid =[[2, 1, 1, 0, 1], [1, 2, 0, 3, 0], [0, 1, 5, 1, 2], [0, 0, 1, 3, 1], [1, 2, 0, 1, 1]]
K = 2
print(solution(grid, K))