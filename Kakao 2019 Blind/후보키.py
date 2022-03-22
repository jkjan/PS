from itertools import combinations


def solution(relation):
    col_num = len(relation[0])
    candidate_keys = []
    cols = [x for x in range(col_num)]

    for n in range(1, col_num + 1):
        col_comb = combinations(cols, n)

        for selected_cols in col_comb:
            key = is_key(selected_cols, relation)

            if key:
                if n == 1:
                    candidate_keys.append(selected_cols)
                else:
                    if sum([set(c_key).issubset(set(selected_cols)) for c_key in candidate_keys]) == 0:
                        candidate_keys.append(selected_cols)

    return len(candidate_keys)


def is_key(selected_cols, relation):
    instance_set = set()

    for r in relation:
        to_add = ""
        for col in selected_cols:
            to_add += (r[col] + '|')
        instance_set.add(to_add)

    return len(instance_set) >= len(relation)


relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]

print(solution(relation))