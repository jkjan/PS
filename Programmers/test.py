# n = int(input())

dp = [-1 for _ in range(51)]

init_cnt = {
    2: 1,
    3: 1,
    4: 1,
    5: 3,
    6: 3,
    7: 1
}

def get_dp(n, a):
    if dp[a] != -1:
        return dp[a]

    if a in init_cnt.keys():
        dp[a] = init_cnt[a]
    else:
        dp[a] = 0

    for i in range(2, a - 1):
        left = get_dp(n + 1, i)
        right = get_dp(n + 1, a - i)

        if n == 1 and i == 6:
            left -= 1

        dp[a] += (left * right)

    for i in range(2, a//2):
        j = a // i
        if a % i == 0 and j > 2:
            if a == 9:
                print(i, j, dp[i])
            dp[a] -= (dp[i] * (j - 2))

    return dp[a]


k = int(input())
dp[1] = 0
print(get_dp(1, k))
print(dp)
