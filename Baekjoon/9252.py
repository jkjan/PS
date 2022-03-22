def solution():
    MAX = 1000

    def get_lcs(ai, bi):
        if dp[ai][bi] == '':
            dp[ai][bi] = a[ai]

            for i in range(ai + 1, a_len):
                if a[i] == b[bi]:
                    ret = get_lcs(i, bi)
                    if len(dp[ai][bi]) < len(ret) + 1:
                        dp[ai][bi] = a[ai] + ret

            for i in range(bi + 1, b_len):
                if a[ai] == b[i]:
                    ret = get_lcs(ai, i)
                    if len(dp[ai][bi]) < len(ret) + 1:
                        dp[ai][bi] = b[ai] + ret



        return dp[ai][bi]

    a = 'z' + input()
    b = 'z' + input()
    a_len = len(a)
    b_len = len(b)
    dp = [['' for _ in range(MAX + 1)] for _ in range(MAX + 1)]
    lcs = get_lcs(0, 0)
    print(len(lcs) - 1)
    if lcs[1:]:
        print(lcs[1:])


solution()