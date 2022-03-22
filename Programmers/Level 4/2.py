from collections import Counter
import re


def solution(words, queries):
    possible = Counter()
    start_min = end_min = float("inf")
    start_max = end_max = -1

    for query in queries:
        start = re.search("^\?*", query).span()
        end = re.search("\?*$", query).span()
        start = start[1] - start[0]
        end = end[1] - end[0]

        if start != 0:
            start_max = max(start_max, start)
            start_min = min(start_min, start)
        if end != 0:
            end_max = max(end_max, end)
            end_min = min(end_min, end)

    for word in words:
        n = len(word)
        possible['?' * n] += 1
        for i in range(start_min, min(start_max + 1, n)):
            possible['?' * i + word[i:]] += 1
        for i in range(end_min, min(end_max + 1, n)):
            possible[word[:n-i] + '?' * i] += 1

    answer = [possible[query] for query in queries]
    return answer


