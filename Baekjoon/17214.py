import re
import sys


def solution():
    p = sys.stdin.readline().strip()
    if p == '0':
        sys.stdout.write('W')
        return

    reed = re.search("(-?)(\d+)(x?)(([+-])(\d+))?", p).groups()

    answer = reed[0] + integral(int(reed[1]), len(reed[2]))

    if reed[3] is not None:
        answer += "%s%s" % (reed[4], integral(int(reed[5]), 0))

    answer += '+W'

    sys.stdout.write(answer)


def integral(coefficient, exp):
    if coefficient == 0:
        return ''
    coefficient //= (exp + 1)
    return ('' if coefficient == 1 else str(coefficient)) + ('x' * (exp + 1))


solution()