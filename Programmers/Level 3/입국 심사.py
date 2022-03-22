# https://programmers.co.kr/learn/courses/30/lessons/43238#

def solution(n, times):
    times.sort()
    fastest = 1
    slowest = times[-1] * n
    while fastest <= slowest:
        m = (fastest + slowest) // 2
        capacity = 0
        for t in times:
            capacity += m // t
        if capacity >= n:
            slowest = m - 1
        elif capacity < n:
            fastest = m + 1
    return fastest

n = 6
times = [7, 10]

print(solution(n, times))