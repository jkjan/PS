import sys

N, S = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

left = 0
right = 0
now_sum = 0
min_len = len(arr) + 1

while left <= right <= len(arr):
    if now_sum < S:
        if right == len(arr):
            break
        now_sum += arr[right]
        right += 1
    else:
        min_len = min(right - left, min_len)
        now_sum -= arr[left]
        left += 1


if min_len == len(arr) + 1:
    print(0)
else:
    print(min_len)