import re
import sys

scan = sys.stdin.readline

def solution():
    T = int(scan())
    for t in range(T):
        tc()



def tc():
    members = scan().strip()
    fans = scan().strip()

    pattern = "(%s)+\1" % "".join(["(M|F)" if m == 'F' else 'F' for m in members])
    print(pattern)
    print(re.findall(pattern, fans))



solution()