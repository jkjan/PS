import sys


now_feet = [0, 0]
power = 0

def solution():
    get_commands()
    for cmd in commands:
        move_to(cmd)
        print(cmd, now_feet)
    sys.stdout.write("%d" % power)


def get_commands():
    global commands
    commands = list(map(int, sys.stdin.readline().split()))[:-1]
    return commands


def move_to(x):
    moved = move_if_possible(x, x, 1)

    if not moved:
        moved = move_if_possible(0, x, 2)

    left = 4 if x == 1 else (x - 1)
    right = 1 if x == 4 else (x + 1)

    moved = decide_left_or_right(left, right)

    if not moved:
        move_if_possible(x + (-1 if x > 2 else 1) * 2, x, 4)


def decide_left_or_right(left, right, x):
    foot_in_left = find_foot_in(left)
    foot_in_right = find_foot_in(right)

    if foot_in_left == foot_in_right:
        if foot_in_right == -1:
            return False
        move_from_to(foot_in_left, x, 3)
    elif foot_in_left != -1 and foot_in_right != -1:
        # TODO: 선택 로직
        pass
    elif foot_in_left != -1:
        move_from_to(foot_in_left, x, 3)
    else:
        move_from_to(foot_in_left, x, 3)

    return True




def find_foot_in(target):
    # TODO: 같은 발 금지 로직
    for i in range(2):
        if now_feet[i] == target:
            return i
    return -1


def move_if_possible(from_, _to, d_power):
    global power
    found_step = find_foot_in(from_)
    if found_step != -1:
        # power += d_power
        # now_feet[found_step] = _to
        move_from_to(found_step, _to, d_power)
        return True
    return False


def move_from_to(from_, _to, d_power):
    global power
    power += d_power
    now_feet[from_] = _to

solution()
