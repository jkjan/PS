import sys


def solution():
    A, P = get_input()
    duplicated = {A: 0}
    last_num = A
    i = 1

    while True:
        new_num = get_next(last_num, P)
        if new_num in duplicated.keys():
            print(duplicated[new_num])
            return
        duplicated[new_num] = i
        i += 1
        last_num = new_num


def get_input():
    A, P = map(int, sys.stdin.readline().split())
    return A, P


def get_next(last_num, P):
    new_num = 0
    while 0 < last_num:
        new_num += (last_num % 10) ** P
        last_num //= 10
    return new_num


solution()


