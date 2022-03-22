import math
from collections import defaultdict


def solution(fees, records):
    car_log = defaultdict(lambda: [])
    cars_fee = []

    for r in records:
        timestamp, car_num, in_or_out = r.split()
        car_log[car_num].append(timestamp)

    for c, log in car_log.items():
        total_time = 0
        log.sort()

        for i in range(0, len(log), 2):
            in_time = log[i]

            if i + 1 == len(log):
                out_time = "23:59"
            else:
                out_time = log[i+1]

            total_time += elapsed_time(in_time, out_time)

        if total_time <= fees[0]:
            total_fee = fees[1]
        else:
            total_fee = fees[1] + math.ceil((total_time - fees[0]) / fees[2]) * fees[3]
        cars_fee.append((c, total_fee))

    cars_fee.sort()

    return [cars_fee[i][1] for i in range(len(cars_fee))]


def to_unix_time(t):
    h, m = t.split(":")
    return int(h) * 60 + int(m)

def elapsed_time(in_time, out_time):
    in_time = to_unix_time(in_time)
    out_time = to_unix_time(out_time)
    return out_time - in_time


fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]

print(solution(fees, records))
