def solution(N, stages):
    stages.sort()
    summary = {}

    s, e = 0, 0

    while e < len(stages):
        if stages[s] != stages[e]:
            summary[stages[s]] = (s, e)
            s = e
        e += 1

    summary[stages[s]] = (s, e)


    failure_rate = []
    for i in range(1, N + 1):
        if i not in summary.keys():
            failure_rate.append((i, 0))
        else:
            s, e = summary[i]
            failure_rate.append((i, (e - s) / (len(stages) - s)))

    answer = [stage_num for stage_num, rate in sorted(failure_rate, key=lambda x: -x[1])]
    return answer






N = 4
stages = [4,4,4,4]
solution(N, stages)