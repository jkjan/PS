from collections import deque


def solution(n, k, cmd):
    table = [i for i in range(n)]
    is_erased = [False for i in range(n)]
    erased = deque()
    now_len = n

    def U(x):
        nonlocal k
        k -= x
        if k < 0:
            k = 0

    def D(x):
        nonlocal k
        k += x
        if k >= now_len:
            k = now_len - 1

    def C():
        nonlocal table, now_len
        erased.append((k, table[k]))
        is_erased[table[k]] = True
        table = table[:k] + (table[k+1:] if k+1 < now_len else [])
        now_len -= 1

    def Z():
        nonlocal table, now_len
        row, value = erased.pop()
        is_erased[value] = False
        table = table[:row] + [value] + (table[row:] if row < now_len else [])
        now_len += 1


    for c in cmd:
        cc = c.split(" ")
        if c[0] == 'D':
            D(int(cc[1]))
        elif c[0] == 'U':
            U(int(cc[1]))
        elif c[0] == 'C':
            C()
        else:
            Z()
        print(table)

    answer = ''
    for e in is_erased:
        answer += ("X" if e else "O")

    return answer


n = 8
k = 2
cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]

print(solution(n, k, cmd))