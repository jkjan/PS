import sys
import re
from collections import deque


def solution():
    T = int(sys.stdin.readline())

    for t in range(T):
        sys.stdout.write("%s\n" % tc())


def tc():
    p, arr = get_input()
    df = 1

    for command in p:
        if command == 'R':
            df *= -1
        else:
            if len(arr) == 0:
                return "error"
            if df == 1:
                arr.popleft()
            else:
                arr.pop()

    answer = []
    while len(arr) > 0:
        if df == 1:
            answer.append(arr.popleft())
        else:
            answer.append(arr.pop())

    return '[' + ",".join(answer) + ']'


def get_input():
    p = sys.stdin.readline().strip()
    _ = sys.stdin.readline()
    arr = sys.stdin.readline().strip()
    arr = deque(re.findall("\d+", arr))
    return p, arr


solution()