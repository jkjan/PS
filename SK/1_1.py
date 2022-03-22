from collections import defaultdict



def get_token(tokens, word):
    n = len(word)
    for size in range(1, n + 1):
        for i in range(n - size + 1):
            tokens[word[i:i+size]].add(word)


def solution(goods):
    tokens = defaultdict(set)
    unique = [[] for _ in range(len(goods))]
    goods_to_idx = {}
    answer = []

    for i in range(len(goods)):
        goods_to_idx[goods[i]] = i

    for word in goods:
        get_token(tokens, word)

    for k, v in tokens.items():
        if len(v) == 1:
            for w in v:
                unique[goods_to_idx[w]].append(k)

    for i in range(len(goods)):
        min_len = len(goods[i])
        min_unique = []
        unique[i].sort()

        for j in range(len(unique[i])):
            if len(unique[i][j]) < min_len:
                min_len = len(unique[i][j])
                min_unique = [unique[i][j]]
            elif len(unique[i][j]) == min_len:
                min_unique.append(unique[i][j])

        if len(min_unique) > 0:
            answer.append(" ".join(min_unique))
        else:
            answer.append("None")

    return answer


goods =["abcdeabcd","cdabe","abce","bcdeab"]
print(solution(goods))
