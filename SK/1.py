import heapq


def solution(money, costs):
    coins = [1, 5, 10, 50, 100, 500]
    values = [(-(coins[i] / costs[i]), coins[i], i) for i in range(6)]
    heapq.heapify(values)
    total = 0

    while money > 0:
        value, coin, idx = heapq.heappop(values)
        value *= -1
        amount, money = divmod(money, coin)
        total += amount * costs[idx]

    return total


money = 1999
costs= [2, 11, 20, 100, 200, 600]
print(solution(money,costs))