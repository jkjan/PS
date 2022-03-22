from itertools import product


day_to_num = {
    "MO": 0, "TU": 1, "WE": 2, "TH": 3, "FR": 4
}

def solution(schedule):
    answer = 0

    candidates = list(product([0, 1, 2, 3], repeat=5))

    for candidate in candidates:
        answer += is_possible(schedule, candidate)

    return answer


def fill_timetable(timetable, day, time, n):
    col = day_to_num[day]
    hh, mm = map(int, [x for x in time.split(':')])

    row = 2 * (hh - 9)
    if mm == 30:
        row += 1

    for i in range(row, row + n):
        if timetable[col][i]:
            return True
        timetable[col][i] = True

    return False


def is_possible(schedule, candidate):
    timetable = [[False for _ in range(25)] for _ in range(5)]

    for i in range(5):
        elapsing = schedule[i][candidate[i]]
        s = elapsing.split()

        dup = 0

        if len(s) == 4:
            dup += fill_timetable(timetable, s[0], s[1], 3)
            dup += fill_timetable(timetable, s[2], s[3], 3)
        else:
            dup += fill_timetable(timetable, s[0], s[1], 6)

        if dup > 0:
            return False

    return True


schedule = [["MO 12:00 WE 14:30", "MO 12:00", "MO 15:00", "MO 18:00"], ["TU 09:00", "TU 10:00", "TU 15:00", "TU 18:00"], ["WE 09:00", "WE 12:00", "WE 15:00", "WE 18:00"], ["TH 09:30", "TH 11:30", "TH 15:00", "TH 18:00"], ["FR 15:00", "FR 15:00", "FR 15:00", "FR 15:00"]]

print(solution(schedule))