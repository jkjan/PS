def solution(s):
    to_num = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }

    answer = ''
    ss = ''

    i = 0
    while i < len(s):
        if ord('0') <= ord(s[i]) <= ord('9'):
            answer += s[i]
        else:
            ss += s[i]
            if ss in to_num.keys():
                answer += to_num[ss]
                ss = ''

        i += 1

    return answer


s = "23four5six7"
print(solution(s))