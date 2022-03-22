from collections import Counter


def special_sort(linear_A):
    counter = Counter(linear_A)
    count_tuples = sorted([(x, x_cnt) for x, x_cnt in counter.items()], key=lambda x: (x[1], x[0]))
    sorted_A = []
    for x, x_cnt in count_tuples:
        sorted_A += [x, x_cnt]
    return sorted_A


def R(A):
    for i in range(len(A)):
        sorted_A = special_sort(A[i])
        A[i] = sorted_A


def C(A):
    for j in range(len(A)):
        linear_A = [A[i][j] for i in range(len(A))]


A = [3, 1, 1]
print(special_sort(A))