# https://programmers.co.kr/learn/courses/30/lessons/67258
from collections import Counter


def solution(gems):
    gem_types = len(set(gems))
    min_len = len(gems) + 1
    s = e = 0
    start = 0
    while True:
        this_s, this_e = spread(start, gems, gem_types)
        if this_s == -1:
            break
        this_len = this_e - this_s + 1
        start = this_s + 1
        if this_len < min_len:
            s, e, min_len = this_s, this_e, this_len
    return s + 1, e + 1


def spread(from_, gems, gem_types):
    unique_gems = Counter()
    s = from_
    e = from_

    included_all = False
    while e < len(gems):
        unique_gems[gems[e]] += 1
        if len(unique_gems) == gem_types:
            included_all = True
            break
        e += 1

    if not included_all:
        return -1, -1

    while len(unique_gems) == gem_types:
        unique_gems[gems[s]] -= 1
        if unique_gems[gems[s]] == 0:
            unique_gems.pop(gems[s])
        s += 1

    return s-1, e


gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]

print(solution(gems))