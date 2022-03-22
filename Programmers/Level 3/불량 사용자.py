# https://programmers.co.kr/learn/courses/30/lessons/64064

import re
from collections import deque


def solution(user_ids, banned_ids):
    every_possible_banned = []
    for banned_id in banned_ids:
        possible_banned = find_possible_banned(user_ids, banned_id)
        every_possible_banned.append(possible_banned)
    cnt = bfs(every_possible_banned)
    return cnt


def find_possible_banned(user_ids, banned_id):
    possible_banned = []
    for user_id in user_ids:
        if is_match(user_id, banned_id):
            possible_banned.append(user_id)
    return possible_banned


def is_match(user_id, banned_id):
    if len(user_id) != len(banned_id):
        return False
    banned_regex = banned_id.replace('*', '.')
    return re.match(banned_regex, user_id) is not None


def bfs(every_possible_banned):
    will_visit = deque()
    will_visit.append((frozenset(), 0))
    cases = set()

    while 0 < len(will_visit):
        case, idx = will_visit.popleft()
        if idx == len(every_possible_banned):
            cases.add(case)
            continue
        for possible_id in every_possible_banned[idx]:
            if possible_id not in case:
                will_visit.append((case.union({possible_id}), idx + 1))
    return len(cases)


user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["fr*d*", "*rodo", "******", "******"]

print(solution(user_id, banned_id))