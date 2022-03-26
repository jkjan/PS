from collections import defaultdict
from itertools import combinations


def solution(sentences, n):
    answer = -1
    keys_required = [set() for _ in range(len(sentences))]
    score_for_key = defaultdict(lambda : 0)
    scores = [get_score(sent) for sent in sentences]

    for i, sent in enumerate(sentences):
        for a in sent:
            if a.isalpha():
                if a.isupper():
                    keys_required[i].add('shift')
                keys_required[i].add(a.lower())

    for i, sent in enumerate(sentences):
        for a in keys_required[i]:
            score_for_key[a] += scores[i]


    score_for_key = sorted(score_for_key.items(), key=lambda x: -x[1])
    print(score_for_key)
    score_for_key = score_for_key[:min(n, len(score_for_key))]
    selected_keys = set([x[0] for x in score_for_key])
    print(selected_keys)

    answer = 0
    for i, sent in enumerate(sentences):
        possible = True
        for a in sent:
            if a.isalpha():
                if a.isupper():
                    if "shift" not in selected_keys:
                        possible = False
                        break
                if a.lower() not in selected_keys:
                    possible = False
                    break
        if possible:
            answer += scores[i]

    return answer


def get_score(sent):
    score = len(sent)
    for a in sent:
        if a.isupper():
            score += 1
    return score



sentences = ["ABcD", "bdbc", "a", "Line neWs"]
n = 5
print(solution(sentences, n))
# print("a".isupper())