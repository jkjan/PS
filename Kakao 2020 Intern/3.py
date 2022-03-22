def solution(gems):
    for_now = {}
    s, e = 1, 1
    for_now[gems[0]] = 1
    for i, g in enumerate(gems[1:]):
        if g not in for_now.keys():
            s = min([v for v in for_now.values()])
            e = i + 2
        for_now[g] = i + 2

    return [s, e]