import sys
import re


scan = sys.stdin.readline

def solution():
    C = int(scan())
    for c in range(C):
        tc()


def tc():
    pattern = '^' + scan().strip() + '$'
    pattern = pattern.replace("*", ".*")
    pattern = pattern.replace("?", ".")
    N = int(scan())
    matched = []
    for n in range(N):
        file_name = scan().strip()
        if re.match(pattern, file_name) is not None:
            matched.append(file_name)
    matched.sort()
    for m in matched:
        sys.stdout.write("%s\n" % m)


solution()