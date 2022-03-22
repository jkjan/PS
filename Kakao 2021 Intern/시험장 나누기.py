import math
import sys


def solution(k, num, links):
    sys.setrecursionlimit(100001)

    def pre_order(node, limit):
        if node == -1:
            return 0, 0

        left_sum, left_group = pre_order(links[node][0], limit)
        right_sum, right_group = pre_order(links[node][1], limit)

        subtree_sum = left_sum + right_sum + num[node]
        group_sum = left_group + right_group

        if subtree_sum <= limit:
            possible_sum = subtree_sum
            possible_group = group_sum
        else:
            smaller_child = min(left_sum, right_sum)
            cut_one = smaller_child + num[node]

            if cut_one <= limit:
                possible_sum = cut_one
                possible_group = group_sum + 1
            elif num[node] <= limit:
                possible_sum = num[node]
                possible_group = group_sum + 2
            else:
                possible_sum = math.inf
                possible_group = math.inf

        return possible_sum, possible_group


    def get_root():
        is_root = [True for _ in range(len(num))]

        for link in links:
            for child in link:
                if child != -1:
                    is_root[child] = False

        return max(range(len(is_root)), key=lambda i: is_root[i])

    s = max(num)
    e = sum(num)
    root = get_root()

    while s <= e:
        m = (s + e) // 2
        _, k_here = pre_order(root, m)

        if k_here < k:
            e = m - 1
        else:
            s = m + 1

    return s




k = 4
num = [6, 9, 7, 5]
links = [[-1, -1], [-1, -1], [-1, 0], [2, 1]]

print(solution(k, num, links))
#
# l = [1, 2, 3, 3, 3, 5, 5, 5, 5]
# ll = [(i, l[i]) for i in range(len(l))]
#
# s = 0
# e = len(ll) - 1
# k = 4
#
# while s <= e:
#     m = (s + e) // 2
#     if ll[m][1] <= k:
#         s = m + 1
#     else:
#         e = m - 1
#
#
# print(ll[e])