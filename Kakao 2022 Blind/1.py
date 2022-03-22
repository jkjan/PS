from collections import Counter, defaultdict


def solution(id_list, report, k):
    users_reported_by = defaultdict(lambda : set())
    reported_cnt = Counter()
    answer = []

    for r in report:
        report_once(users_reported_by, reported_cnt, r)


    for user_id in id_list:
        mail_cnt = 0
        if user_id in users_reported_by.keys():
            for reported_user in users_reported_by[user_id]:
                if reported_cnt[reported_user] >= k:
                    mail_cnt += 1
        answer.append(mail_cnt)

    return answer



def report_once(users_reported_by, reported_cnt, r):
    user_id, reporting_id = r.split()

    if reporting_id not in users_reported_by[user_id]:
        users_reported_by[user_id].add(reporting_id)
        reported_cnt[reporting_id] += 1



k = 3
id_list = ["con", "ryan"]
report = ["ryan con", "ryan con", "ryan con", "ryan con"]

print(solution(id_list, report, k))