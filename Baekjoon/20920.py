import sys
from collections import Counter

N, M = map(int, sys.stdin.readline().split())
word_count = Counter()
word_set = []

for i in range(N):
    word = sys.stdin.readline().strip()
    word_count[word] += 1
    if word_count[word] == 1 and M <= len(word):
        word_set.append(word)


word_set.sort(key=lambda x: (-word_count[x], -len(x), x))

sys.stdout.write("%s" % "\n".join(word_set))