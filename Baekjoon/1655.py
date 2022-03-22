import sys
from queue import PriorityQueue


N = int(sys.stdin.readline().strip())

max_heap = PriorityQueue()
min_heap = PriorityQueue()


for i in range(N):
    num = int(sys.stdin.readline().strip())

    if max_heap.empty():
        max_heap.put(-num)
    elif len(max_heap.queue) == len(min_heap.queue):
        max_heap.put(-num)
    else:
        min_heap.put(num)

    if not max_heap.empty() and not min_heap.empty() and not (-max_heap.queue[0] <= min_heap.queue[0]):
        a = -max_heap.get()
        b = min_heap.get()
        min_heap.put(a)
        max_heap.put(-b)

    sys.stdout.write("%d\n" % -max_heap.queue[0])
