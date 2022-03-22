import sys


scan = sys.stdin.readline
connected = [
    [0, 1, 2],
    [3, 7, 9, 11],
    [4, 10, 14, 15],
    [0, 4, 5, 6, 7],
    [6, 7, 8, 10, 12],
    [0, 2, 14, 15],
    [3, 14, 15],
    [4, 5, 7, 14, 15],
    [1, 2, 3, 4, 5],
    [3, 4, 5, 9, 13],
]



def solution():
    T = int(scan())
    for t in range(T):
        sys.stdout.write("%d\n" % tc())


def tc():
    def dfs(switch):
        if switch == 10:
            if sum(clock) == 0:
                return 0
            else:
                return float("inf")

        min_cnt = float("inf")
        for i in range(4):
            min_cnt = min(min_cnt, i + dfs(switch + 1))
            push(switch)
        return min_cnt


    def push(switch):
        for i in connected[switch]:
            clock[i] = (clock[i] + 3) % 12


    clock = list(map(lambda x: int(x) % 12, scan().strip().split()))
    answer = dfs(0)
    if answer == float("inf"):
        return -1
    else:
        return answer


solution()