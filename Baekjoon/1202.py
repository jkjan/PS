import sys, heapq


scan = sys.stdin.readline

def solution():
    gems, bags = get_input()
    maximum_price = 0
    gems_available = []

    while 0 < len(bags):
        bag = heapq.heappop(bags)

        while 0 < len(gems) and gems[0][0] <= bag:
            heapq.heappush(gems_available, -gems[0][1])
            heapq.heappop(gems)

        if 0 < len(gems_available):
            maximum_price -= heapq.heappop(gems_available)

    sys.stdout.write("%d" % maximum_price)


def get_input():
    N, K = map(int, scan().split())

    gems = []
    for i in range(N):
        M, V = map(int, scan().split())
        heapq.heappush(gems, (M, V))

    bags = []
    for i in range(K):
        C = int(scan().strip())
        heapq.heappush(bags, C)

    return gems, bags


solution()

"""
4 4
1 100
2 200
13 300
10 500
10
10
10
14
"""