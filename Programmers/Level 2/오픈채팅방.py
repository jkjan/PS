def solution(record):
    user_name = {}

    split_log = []
    answer = []

    for rec in record:
        split = rec.split()
        split_log.append(split[:2])

        try:
            [_, uid, nickname] = split
            user_name[uid] = nickname
        except ValueError:
            pass

    for op, uid in split_log:
        if op == "Enter":
            answer.append("%s님이 들어왔습니다." % user_name[uid])
        elif op == "Leave":
            answer.append("%s님이 나갔습니다." % user_name[uid])


    return answer




record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]

print(solution(record))