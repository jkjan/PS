import re


def solution(s):
    tuple_strings = re.findall("{([\d+,?]+)}", s)
    tuples = []

    for t in tuple_strings:
        t = list(map(int, t.split(",")))
        tuples.append(t)

    tuples.sort(key=lambda x: len(x))

    answer = []
    num_set = set()

    for t in tuples:
        for num in t:
            if num not in num_set:
                answer.append(num)
                num_set.add(num)

    return answer


s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
solution(s)