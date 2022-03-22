from itertools import permutations
from copy import copy


def get_exp(expression):
    n = 0
    operands = {}
    exp = []
    for e in expression:
        try:
            n += int(e)
            n *= 10
        except ValueError:
            n = n // 10
            exp.append(n)
            n = 0

            if e not in operands.keys():
                operands[e] = []
            operands[e].append(len(exp))
            exp.append(e)

    n = n // 10
    exp.append(n)
    return exp, operands


def get_permutation(operands):
    return [i for i in permutations([j for j in operands], len(operands))]


def find_left(exp, l):
    for i in range(l-1, -1, -1):
        if isinstance(exp[i], int):
            return i


def find_right(exp, r):
    for i in range(r+1, len(exp), 1):
        if isinstance(exp[i], int):
            return i


def calc_with_priority(priority, exp, operands):
    for p in priority:
        for o in operands[p]:
            left = find_left(exp, o)
            right = find_right(exp, o)
            if p == '-':
                res = exp[left] - exp[right]
            elif p == '*':
                res = exp[left] * exp[right]
            else:
                res = exp[left] + exp[right]
            exp[left] = exp[right] = '!'
            exp[o] = res

    return res


def solution(expression):
    exp, operands = get_exp(expression)
    perm = get_permutation(operands.keys())
    prize = 0

    for p in perm:
        res = calc_with_priority(p, copy(exp), operands)
        res = abs(res)
        if res > prize:
            prize = res
    return prize