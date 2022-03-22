def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


def lcm(x, y):
    return x * y // gcd(x, y)


def solution(mod1, mod2, max_range):
    answer = (max_range // mod1) - (max_range // lcm(mod1, mod2))
    return answer
