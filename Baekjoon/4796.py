import sys


i = 1
while True:
    L, P, N = map(int, sys.stdin.readline().split())
    if L == 0:
        break
    t, r = divmod(N, P)
    sys.stdout.write("Case %d: %d\n" % (i, t * L + min(r, L)))
    i += 1
