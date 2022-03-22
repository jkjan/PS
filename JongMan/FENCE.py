import sys

scan = sys.stdin.readline


def solution():
    T = int(scan())
    for t in range(T):
        tc()


def tc():
    N = int(scan())
    fence = list(map(int, scan().strip().split()))

    def solve(l, r):
        if l == r:
            return fence[l]

        mid = (l + r) // 2
        ret = max(solve(l, mid), solve(mid + 1, r))

        lo, hi = mid, mid + 1
        s = min(fence[lo], fence[hi])
        ret = max(ret, s * 2)

        while l < lo or hi < r:
            if hi < r and (lo == l or fence[lo - 1] < fence[hi + 1]):
                hi += 1
                s = min(s, fence[hi])
            else:
                lo -= 1
                s = min(s, fence[lo])
            ret = max(ret, s * (hi - lo + 1))

        return ret


    sys.stdout.write("%d\n" % solve(0, N-1))


solution()