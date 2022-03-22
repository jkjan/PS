import copy


def solution(triangle):
    dp_triangle = copy.deepcopy(triangle)
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            dp_triangle[i][j] += max(dp_triangle[i-1][j-1] if j-1 >= 0 else 0,
                                     dp_triangle[i-1][j] if j < len(dp_triangle[i-1]) else 0)

    return max(dp_triangle[-1])


triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print(solution(triangle))