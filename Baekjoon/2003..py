import sys


N, M = map(int, sys.stdin.readline().split())

A = list(map(int, sys.stdin.readline().split()))

left = 0
right = 0
now_sum = 0
cnt = 0
while left <= right <= N:
    if now_sum >= M:
        if now_sum == M:
            cnt += 1
        now_sum -= A[left]
        left += 1
    else:
        if right == N:
            break
        now_sum += A[right]
        right += 1

print(cnt)