import heapq
import sys
from collections import Counter


def solution():
    global min_heap, max_heap, min_max_heap, available

    T = int(sys.stdin.readline())
    for t in range(T):
        min_heap = []
        max_heap = []
        min_max_heap = [[], max_heap, min_heap]
        available = Counter()
        sys.stdout.write(tc() + '\n')


def tc():
    k = int(sys.stdin.readline())

    for i in range(k):
        command = sys.stdin.readline().split()
        head, num = command[0], int(command[1])

        if head == 'I':
            I(num)
        else:
            D(num)

    max_ = get_top(1)
    min_ = get_top(-1)

    if max_ is None or min_ is None:
        return "EMPTY"
    else:
        return "%d %d" % (max_, min_)


def I(x):
    heapq.heappush(min_heap, x)
    heapq.heappush(max_heap, -x)
    available[x] += 1


def D(x):
    top = get_top(x)

    if top is not None:
        heapq.heappop(min_max_heap[x])
        available[top] -= 1


def get_top(x):
    while len(min_max_heap[x]) > 0:
        top = -x * min_max_heap[x][0]
        if available[top] > 0:
            return top
        heapq.heappop(min_max_heap[x])

    return None


solution()