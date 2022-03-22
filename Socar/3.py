from collections import Counter

INF = 1000000000

sabun = [(1, 1), (0, 1), (0, 0), (1, 0)]

def search(arr, x):
    s = 0
    e = len(arr) - 1
    while s <= e:
        m = (s + e) // 2
        if arr[m] == x:
            return m
        elif arr[m] > x:
            e = m - 1
        else:
            s = m + 1
    return -1

def get_sabun(x, y):
    s = (x >= 0, y >= 0)
    return sabun.index(s)


def solution(monsters, bullets):
    _monsters = [set() for _ in range(4)]

    monsters_cnt = [Counter() for _ in range(4)]
    for mx, my in monsters:
        ml = my/mx if mx != 0 else INF
        s = get_sabun(mx, my)
        monsters_cnt[s][ml] += 1
        _monsters[s].add(ml)

    bullets = [((b/a, a, b) if a != 0 else (INF, a, b))  for [a, b] in bullets]

    for i in range(4):
        _monsters[i] = sorted(_monsters[i])

    answer = 0
    for b, x, y in bullets:
        s = get_sabun(x, y)
        idx = search(_monsters[s], b)

        if idx == -1: continue

        ml = _monsters[s][idx]

        if monsters_cnt[s][ml] >= 1:
            monsters_cnt[s][ml] -= 1
            answer += 1

    return answer



monsters =[[1,2],[-2,-1],[1,-2],[3,-1]]
bullets =[[1,0],[2,1]]

print(solution(monsters, bullets))