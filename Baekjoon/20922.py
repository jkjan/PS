import sys
from collections import Counter

N, K = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

s = 0
e = 0
max_len = 0

num_dup = Counter()

while s < len(arr) and e < len(arr):
    if num_dup[arr[e]] >= K:
        max_len = max(max_len, e - s)
        num_dup[arr[s]] -= 1
        s += 1
    else:
        num_dup[arr[e]] += 1
        e += 1

max_len = max(max_len, e - s)

print(max_len)