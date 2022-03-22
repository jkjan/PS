import sys

N, K = map(int, sys.stdin.readline().split())
letters = [i for i in range(N + 1)]


def make_k(k, s):
    global letters
    k = min(k, len(letters) - 1 - s)
    i = s + k
    letters = letters[:s] + [letters[i]] + letters[s:i] + letters[i+1:]
    return k


s = 1
while 0 < K:
    k = make_k(K, s)
    s += 1
    K -= k

print(" ".join([str(l) for l in letters[1:]]))