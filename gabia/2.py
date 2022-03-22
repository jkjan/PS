import re


def solution(p):
    left = re.search("^<*", p).span()[1]
    s, e = re.search(">*$", p).span()
    right = e - s
    return left + right


p = "<><"
solution(p)