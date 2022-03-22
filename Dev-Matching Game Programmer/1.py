def solution(purchase):
    get_dates()
    total = [0 for _ in range(365 + 2)]

    for p in purchase:
        [ymd, amount] = p.split()
        amount = int(amount)
        month, date = map(int, ymd.split("/")[1:])
        idx = get_idx(month, date)
        total[idx] += amount

        if idx + 30 < len(total):
            total[idx + 30] -= amount


    now_total = 0
    answer = [0 for _ in range(5)]
    for i in range(1, 365 + 1):
        now_total += total[i]
        if 0 <= now_total < 10000:
            add_idx = 0
        elif 10000 <= now_total < 20000:
            add_idx = 1
        elif 20000 <= now_total < 50000:
            add_idx = 2
        elif 50000 <= now_total < 100000:
            add_idx = 3
        else:
            add_idx = 4
        answer[add_idx] += 1

    return answer


def get_dates():
    global dates
    temp = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    dates = [0 for _ in range(len(temp))]
    for i in range(1, len(temp)):
        dates[i] = dates[i-1] + temp[i]


def get_idx(month, date):
    return dates[month - 1] + date



purchase = ["2019/01/01 5000", "2019/04/05 10000", "2019/06/10 20000", "2019/08/15 50000", "2019/12/31 100000"]
print(solution(purchase))