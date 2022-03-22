# https://programmers.co.kr/learn/courses/30/lessons/64063

import sys
sys.setrecursionlimit(200001)

def solution(k, room_number):
    room = [-1 for i in range(k + 1)]
    answer = [assign(room, w) for w in room_number]
    return answer


def assign(room, wish):
    if room[wish] == -1:
        assigned = wish
    else:
        assigned = find(room, wish) + 1
    room[assigned] = assigned
    prev_room, next_room = assigned - 1, assigned + 1
    if next_room < len(room) and room[next_room] != -1:
        room[assigned] = room[next_room]
    if 0 <= prev_room and room[prev_room] != -1:
        room[prev_room] = room[assigned]
    return assigned


def find(room, x):
    if x == room[x]:
        return x
    room[x] = find(room, room[x])
    return room[x]


k = 10
room_number = [1,3,4,1,3,1]

print(solution(k, room_number))