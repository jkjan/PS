from collections import Counter, defaultdict


def solution(orders, course):
    course_to_get = [False for _ in range(11)]
    for c in course:
        course_to_get[c] = True

    total_combination = []

    for order in orders:
        combination = get_combination(order, course_to_get, course[-1])
        total_combination += combination

    counted = count_combinations(total_combination)

    most_picked = pick_most_common(counted)
    most_picked.sort()
    return most_picked


def get_combination(order, course_to_get, max_course):
    order = sorted(order)
    combinations = []

    def dfs(now_idx):
        if len(now_idx) > max_course:
            return
        if course_to_get[len(now_idx)]:
            combined_string = "".join([order[idx] for idx in now_idx])
            combinations.append(combined_string)

        last_idx = -1 if len(now_idx) == 0 else now_idx[-1]
        for i in range(last_idx + 1, len(order)):
            dfs(now_idx + [i])

    dfs([])

    return combinations


def count_combinations(total_combination):
    counted = defaultdict(lambda: Counter())

    for combination in total_combination:
        counted[len(combination)][combination] += 1

    return counted


def pick_most_common(counted):
    most_picked = []

    for comb_counts in counted.values():
        max_count = 0
        max_combinations = []

        for k, v in comb_counts.items():
            if v == max_count:
                max_combinations.append(k)
            if v > max_count:
                max_combinations = [k]
                max_count = v

        if max_count >= 2:
            most_picked += max_combinations

    return most_picked


orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2, 3, 4]


print(solution(orders, course))