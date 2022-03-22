def solution(stones, k):
    return dfs(stones, "", k)


def dfs(now_stones, seq, k):
    if now_stones.count(k) == 1 and now_stones.count(0) == len(now_stones) - 1:
        return seq

    for i in range(len(now_stones) - 1, -1, -1):
        next_stones = do(now_stones, i)

        if next_stones is not None:
            ret = dfs(next_stones, seq + str(i), k)
            if ret != "-1":
                return ret

    return "-1"


def do(now_stones, i):
    next_stones = [0 for _ in range(len(now_stones))]

    for j in range(len(now_stones)):
        if i == j:
            next_stones[i] = now_stones[i] + 1
        else:
            if now_stones[j] == 0:
                return None
            next_stones[j] = now_stones[j] - 1

    return next_stones


# len_ = random.randint(2, 8)
# stones = [random.randint(1, 12) for x in range(len_)]
# k = random.randint(1, 24)
#
# print(len_, k, stones)
stones = [10, 7, 9, 8, 11, 8]
k = 8

print(solution(stones, k))