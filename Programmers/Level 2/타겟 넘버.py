from collections import deque


def solution(numbers, target):
    will_visit = deque([[0, 0]])
    answer = 0

    while len(will_visit) > 0:
        [now_number, now_i] = will_visit.popleft()

        if now_i >= len(numbers):
            if now_number == target:
                answer += 1
            continue

        will_visit.append([now_number + numbers[now_i], now_i + 1])
        will_visit.append([now_number - numbers[now_i], now_i + 1])

    return answer


numbers = [1, 1, 1, 1, 1]
target = 3
print(solution(numbers, target))