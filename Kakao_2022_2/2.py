
arr = [1, 2, 3, 4, 10, 3, 9, 8]


def remove_x(arr, x):
    on = len(arr)
    n = on
    i = 0
    while i < n:
        if arr[i] == x:
            for j in range(i + 1, n):
                arr[j - 1] = arr[j]
            n -= 1
        else:
            i += 1

    for i in range(n, on):
        del arr[-1]


remove_x(arr, 3)

print(arr)