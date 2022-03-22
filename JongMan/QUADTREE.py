import sys


scan = sys.stdin.readline


def solution():
    T = int(scan())
    for t in range(T):
        sys.stdout.write("%s\n" % tc())


def tc():
    pic = scan().strip()

    def flip(start):
        if start >= len(pic):
            return [], start
        if pic[start] != 'x':
            return [pic[start]], start + 1
        else:
            now = start + 1
            chars = []
            for i in range(4):
                char, now = flip(now)
                chars.append(char)
            return ['x'] + chars[2] + chars[3] + chars[0] + chars[1], now

    return "".join(flip(0)[0])


solution()
