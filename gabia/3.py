from itertools import combinations


def solution(arr, k, t):
    n = len(arr)
    answer = 0
    for cnt in range(k, n + 1):
        for x in combinations(arr, cnt):
            if sum(x) <= t:
                answer += 1
                
    return answer