from collections import deque


def solution(gold_prices):
    n = len(gold_prices)
    dp = []
    def dfs(i, recently_bought, recently_sold):
        if i < n and

        if recently_bought == -1 and recently_sold - i >= 2:
            dfs(i + 1, gold_prices[i], recently_sold)
        if recently_bought >= 0 and gold_prices[i] - gold_prices[recently_bought] > 0:
            dfs(i + 1, 0, i) + gold_prices[i] - now_gold
        dfs(i + 1, now_gold, recently_sold)


gold_prices = [2, 5, 1, 3, 4]
print(solution(gold_prices))