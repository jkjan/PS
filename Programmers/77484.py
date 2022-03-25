def solution(lottos, win_nums):
    win_nums = set(win_nums)
    min_n = max_n = 0
    for l in lottos:
        if l in win_nums:
            min_n += 1
            max_n += 1
        if l == 0:
            max_n += 1

    answer = [7 - max(1, max_n), 7 - max(1, min_n)]
    return answer