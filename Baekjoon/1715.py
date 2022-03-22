import sys
import heapq


N = int(sys.stdin.readline().strip())
card_list = [int(sys.stdin.readline().strip()) for i in range(N)]
heapq.heapify(card_list)


def min_compare_count():
    n = 0
    while True:
        comp1 = heapq.heappop(card_list)
        if len(card_list) == 0:
            return 0
        comp2 = heapq.heappop(card_list)
        compared = comp1 + comp2
        n += compared
        if len(card_list) == 0:
            break
        heapq.heappush(card_list, comp1 + comp2)
    return n

sys.stdout.write(str(min_compare_count()))
