import sys


N = int(sys.stdin.readline())
sol = list(map(int, sys.stdin.readline().split()))
sol.sort()

left = 0
right = len(sol) - 1
min_feature = 2_000_000_001
sol_a = 0
sol_b = 0

while left < right:
    now_sum = sol[left] + sol[right]
    now_feature = abs(now_sum)
    if now_feature < min_feature:
        min_feature = now_feature
        sol_a, sol_b = sol[left], sol[right]
    else:
        if now_sum > 0:
            right -= 1
        else:
            left += 1


print(sol_a, sol_b)