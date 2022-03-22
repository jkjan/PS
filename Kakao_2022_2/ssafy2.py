arr = list(map(int, input().split()))


def sp():
    m = -1

    for i in range(1, len(arr)):
        s1 = get_score(arr[0:i])
        s2 = get_score(arr[i:])

        m = max(m, s1 + s2)

    print(m)


def get_score(a):
    return max(a) - min(a)


sp()