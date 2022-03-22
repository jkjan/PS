
def solution(A):
    consec = 0
    pay = []
    answer = 0

    for a in A:
        consec += a

        if a < 0:
            pay.append(a)

        if consec < 0:
            pay.sort(reverse=True)
            go_back = pay.pop()
            consec -= go_back
            answer += 1

    return answer


A = [10, ]