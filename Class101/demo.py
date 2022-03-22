
def solution(A):
    answer = 1

    is_occurred = [False for _ in range(1_000_001)]

    for a in A:
        if a > 0:
            is_occurred[a] = True
    for i in range(1, len(is_occurred)):
        if not is_occurred[i]:
            answer = i
            break

    return answer
