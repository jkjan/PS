# https://programmers.co.kr/learn/courses/30/lessons/72414
from collections import deque
ad = [0 for i in range(360000)]


def solution(play_time, adv_time, logs):
    answer = ""

    for log in logs:
        start = str_to_sec(log[:8])
        finish = str_to_sec(log[9:])
        for i in range(start, finish):
            ad[i] += 1

    N = str_to_sec(play_time)
    len = str_to_sec(adv_time)

    idx = 0
    sum = 0
    max_sum = 0

    q = deque()

    for i in range(len):
        sum += ad[i]
        q.append(ad[i])

    max_sum = sum

    for i in range(len, N):
        sum += ad[i]
        q.append(ad[i])
        sum -= q.popleft()

        if sum > max_sum:
            idx = i - len + 1
            max_sum = sum

    answer = sec_to_str(idx)
    return answer


def str_to_sec(s):
    ret = 0
    h = s[:2]
    m = s[3:5]
    s = s[6:]

    ret += int(h) * 60 * 60
    ret += int(m) * 60
    ret += int(s)

    return ret


def sec_to_str(n):
    ret = ""

    s = n % 60
    n //= 60
    m = n % 60
    n //= 60
    h = n

    if h < 10:
        ret += "0"
    ret += str(h)
    ret += ":"

    if m < 10:
        ret += "0"
    ret += str(m)
    ret += ":"

    if s < 10:
        ret += "0"
    ret += str(s)

    return ret


play_time = "02:03:55"
adv_time = "00:14:15"
logs = ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30", "02:04:00-02:03:55"]

print(solution(play_time, adv_time, logs))