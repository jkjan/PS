# https://programmers.co.kr/learn/courses/30/lessons/42627
import heapq
from collections import deque


def solution(jobs):
    now = 0
    avg = 0
    total = len(jobs)
    jobs.sort()
    waiting_queue = deque(jobs)
    job_queue = []

    while 0 < len(waiting_queue) or 0 < len(job_queue):
        while 0 < len(waiting_queue):
            point, eta = waiting_queue.popleft()
            if point <= now:
                heapq.heappush(job_queue, (eta, point))
            else:
                waiting_queue.appendleft((point, eta))
                break

        if 0 >= len(job_queue):
            now += 1
            continue

        eta, point = heapq.heappop(job_queue)
        now += eta
        avg += (now - point)

    avg //= total
    return avg


jobs = [[0, 3], [1, 9], [2, 6]]
print(solution(jobs))