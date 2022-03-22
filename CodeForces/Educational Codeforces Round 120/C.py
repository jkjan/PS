import sys


def solution():
    t = int(sys.stdin.readline())
    for i in range(t):
        tc()


def tc():
    n, k, arr = get_input()
    arr.sort()
    total = 0
    cnt = 0
    print(arr)

    for i in range(n):
        total += arr[i]
        if total >= k:
            total -= arr[i]
            total += arr[0]
            cnt += 1

    if total > k:
        cnt += total - k

    sys.stdout.write("%d\n" % cnt)


def get_input():
    n, k = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().split()))
    return n, k, arr


solution()