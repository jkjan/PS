def solution(estimates, k):
    n = len(estimates)
    first = sum(estimates[:k])
    max_sum = first

    for i in range(n - k):
        first -= estimates[i]
        first += estimates[i + k]
        max_sum = max(max_sum, first)

    return max_sum