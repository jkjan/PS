import sys
import heapq


scan = sys.stdin.readline
printf = sys.stdout.write


def solution():
    T = int(scan())
    for t in range(T):
        tc()


def tc():
    K = int(scan())
    chapter_lengths = list(map(int, scan().split()))
    heapq.heapify(chapter_lengths)

    total_cost = 0
    while len(chapter_lengths) > 1:
        chapterA = chapter_lengths[0]; heapq.heappop(chapter_lengths)
        chapterB = chapter_lengths[0]; heapq.heappop(chapter_lengths)
        cost = chapterA + chapterB
        heapq.heappush(chapter_lengths, cost)
        total_cost += cost

    printf("%d\n" % total_cost)


solution()