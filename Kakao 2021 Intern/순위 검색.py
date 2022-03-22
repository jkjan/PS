from collections import defaultdict, deque


def solution(info, query):
    db = defaultdict(lambda: [])

    cases = bfs()

    for insert_query in info:
        instance = insert_query.split()

        for c in cases:
            instance_to_add = ['-' if c[i] else instance[i] for i in range(4)]
            db[" ".join(instance_to_add)].append(int(instance[-1]))

    answers = []

    for v in db.values():
        v.sort()

    for q in query:
        split_query = q.split(" ")
        condition, score = " ".join(split_query[::2]), int(split_query[-1])
        answers.append(len(db[condition]) - find_idx(db[condition], score))

    return answers


def find_idx(sorted_list, x):
    s, e = 0, len(sorted_list)

    while s < e:
        m = (s + e) // 2

        if x <= sorted_list[m]:
            e = m
        else:
            s = m + 1

    return s


def bfs():
    will_visit = deque([[]])
    cases = []

    while len(will_visit) > 0:
        now_visit = will_visit.popleft()

        if len(now_visit) == 4:
            cases.append(now_visit)

        if len(now_visit) > 4:
            break

        will_visit.append(now_visit + [True])
        will_visit.append(now_visit + [False])

    return cases


info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]

query=  ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

print(solution(info, query))