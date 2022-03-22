from itertools import permutations
import sys


def solution():
    t = int(sys.stdin.readline())

    for i in range(t):
        ls = list(map(int, sys.stdin.readline().split()))
        print("YES" if is_possible(ls) else "NO")


def is_possible(ls):
    poss = list(permutations(ls))

    for j in range(len(poss)):
        [a, b, c] = poss[j]
        if (b + c == a) or (b == c and a % 2 == 0):
            return True

    return False


solution()