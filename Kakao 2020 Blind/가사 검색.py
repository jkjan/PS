from collections import Counter


def solution(words, queries):
    answer = []
    possible_word_cnt = Counter()
    query_lens = set([len(q) for q in queries])
    max_question_mark = max([q.count('?') for q in queries])
    min_question_mark = min([q.count('?') for q in queries])

    for word in words:
        if len(word) in query_lens:
            mask_question_mark(possible_word_cnt, word, max_question_mark, min_question_mark)

    for q in queries:
        answer.append(possible_word_cnt[q])

    return answer


def mask_question_mark(possible_word_cnt, word, max_question_mark, min_question_mark):
    n = len(word)

    for i in range(min_question_mark, min(n, max_question_mark + 1)):
        possible_word_cnt['?' * i + word[i:]] += 1
        possible_word_cnt[word[:n - i] + '?' * i] += 1

    if n <= max_question_mark:
        possible_word_cnt['?' * n] += 1


words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]

queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
print(solution(words, queries))