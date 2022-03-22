def solution(n, k, cmd):
    table = [True for _ in range(n)]
    removed = []

    def U(X):
        nonlocal k
        X = int(X)
        i = 0
        while i < X:
            k -= 1
            if table[k]:
                i += 1


    def D(X):
        nonlocal k
        X = int(X)
        i = 0
        while i < X:
            k += 1
            if table[k]:
                i += 1


    def C():
        nonlocal k
        removed.append(k)
        table[k] = False

        if k == n-1:
            k -= 1
        else:
            k += 1


    def Z():
        nonlocal k, removed
        restored = removed[-1]
        table[restored] = True
        removed = removed[:-1]


    for c in cmd:
        c = c.split()
        eval("%s(%s)" % (c[0], (c[1] if len(c) == 2 else "")))

    answer = "".join(['O' if table[i] else 'X' for i in range(n)])

    return answer


n = 8
k = 2
cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]

print(solution(n, k, cmd))