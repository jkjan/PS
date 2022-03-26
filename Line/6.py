import heapq


BUY = 0
SELL = 1

GOLD = 0
SILVER = 1

def solution(req_id, req_info):
    reqs = [[], []]
    diffs = {}
    for id in req_id:
        diffs[id] = [0, 0]

    for i, req in enumerate(req_info):
        # 판매자 등록
        if req[0] == SELL:
            type_, sell_amount, sell_price = req

            while sell_amount > 0:
                # 구매자 없음
                if len(reqs[BUY]) == 0:
                    heapq.heappush(reqs[SELL], (sell_price, i, sell_amount))
                    break

                buy_price, buyer_id, buy_amount = heapq.heappop(reqs[BUY])
                buy_price *= -1

                # 등록 종료
                if buy_price < sell_price:
                    heapq.heappush(reqs[BUY], (-buy_price, buyer_id, buy_amount))
                    heapq.heappush(reqs[SELL], (sell_price, i, sell_amount))
                    break

                amount = min(buy_amount, sell_amount)
                silver_amount = amount * sell_price

                diffs[req_id[i]][GOLD] -= amount
                diffs[req_id[i]][SILVER] += silver_amount
                diffs[req_id[buyer_id]][GOLD] += amount
                diffs[req_id[buyer_id]][SILVER] -= silver_amount

                sell_amount -= amount
                buy_amount -= amount

                if buy_amount > 0:
                    heapq.heappush(reqs[BUY], (-buy_price, buyer_id, buy_amount))

        elif req[0] == BUY:
            type_, buy_amount, buy_price = req

            while buy_amount > 0:
                # 판매자 없음
                if len(reqs[SELL]) == 0:
                    heapq.heappush(reqs[BUY], (-buy_price, i, buy_amount))
                    break

                sell_price, seller_id, sell_amount = heapq.heappop(reqs[SELL])

                # 등록 종료
                if buy_price < sell_price:
                    heapq.heappush(reqs[BUY], (-buy_price, i, buy_amount))
                    heapq.heappush(reqs[SELL], (sell_price, seller_id, sell_amount))
                    break

                amount = min(buy_amount, sell_amount)
                silver_amount = amount * sell_price

                diffs[req_id[i]][GOLD] += amount
                diffs[req_id[i]][SILVER] -= silver_amount
                diffs[req_id[seller_id]][GOLD] -= amount
                diffs[req_id[seller_id]][SILVER] += silver_amount

                sell_amount -= amount
                buy_amount -= amount

                if sell_amount > 0:
                    heapq.heappush(reqs[SELL], (sell_price, seller_id, sell_amount))

    answer = []
    for k, [gold, silver] in diffs.items():
        answer.append(" ".join([k, ('+' if gold > 0 else '') + str(gold), ('+' if silver > 0 else '') + str(silver)]))
    answer.sort()
    return answer




req_id = ["William", "Andy", "Rohan", "Rohan", "Louis", "Andy"]
req_info = [[1, 7, 20], [0, 10, 10], [1, 10, 40], [1, 4, 25], [0, 5, 11], [0, 20, 30]]
print(solution(req_id, req_info))