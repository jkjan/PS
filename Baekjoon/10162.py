T = int(input())

n = 0
n1 = n2 = n3 = 0
if T >= 60 * 5:
    n1, T = divmod(T, 60 * 5)
if T >= 60 * 1:
    n2, T = divmod(T, 60 * 1)
if T >= 10:
    n3, T = divmod(T, 10)

if T == 0:
    print(n1, n2, n3)
else:
    print(-1)