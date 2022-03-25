from math import sqrt


def solution(brown, yellow):
    answer = []
    total = brown + yellow
    half = int(sqrt(total))
    for i in range(2, half + 1):
        if total % i == 0:
            a = total // i
            b = i
            if 2 * a + 2 * b - 4 == brown:
                answer = [a, b]
                break
    return answer


brown = 24
yellow = 24
print(solution(brown, yellow))