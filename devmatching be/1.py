from copy import deepcopy

def solution(dist):
    n = len(dist)
    answer = []

    def get_dp(arr, dist_so_far, used):
        if len(arr) == n:
            answer.append(deepcopy(arr))
            return

        for i in range(0, n):
            if not used[i]:
                if len(arr) == 0:
                    to_add = 0
                    total = 0
                else:
                    to_add = dist[arr[-1]][i]
                    total = dist[arr[0]][i]

                if dist_so_far + to_add == total:
                    used[i] = True
                    arr.append(i)
                    get_dp(arr, total, used)
                    arr.pop()
                    used[i] = False

    get_dp([], 0, [False for _ in range(n)])
    answer.sort()

    return answer


dist = [[0,2,3,1],[2,0,1,1],[3,1,0,2],[1,1,2,0]]
print(solution(dist))