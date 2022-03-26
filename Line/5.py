def solution(abilities, k):
    if len(abilities) % 2 == 1:
        abilities.append(0)
    abilities.sort(reverse=True)

    diffs = [abilities[i] - abilities[i + 1] for i in range(0, len(abilities), 2)]
    diffs = [(i, diffs[i]) for i in range(len(diffs)) if diffs[i] != 0]
    diffs.sort(key=lambda x: -x[1])

    prior = diffs[:k]
    lost = diffs[k:]

    more = sum([prior[i][1] for i in range(len(prior))])
    more -= sum([lost[i][1] for i in range(len(lost))])
    total = sum(abilities)
    return (total + more) // 2


k = 2
abilities = [2, 8, 3, 6, 1, 9, 1, 9]
print(solution(abilities, k))