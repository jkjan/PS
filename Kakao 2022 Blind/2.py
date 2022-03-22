import math
import re


def solution(n, k):
    converted = convert(n, k)
    numbers = get_numbers(converted)
    # limit = int(max(numbers, key=lambda x: (len(x), x))) + 1
    # limit = 20000000
    # is_prime = get_prime(limit)
    is_prime = {1: False}
    answer = 0

    for number in numbers:
        number = int(number)

        if number not in is_prime:
            i = 2
            limit = math.sqrt(number)
            is_prime[number] = True

            while i <= limit:
                if number % i == 0:
                    is_prime[number] = False
                    break
                i += 1

        answer += is_prime[int(number)]

    return answer


def convert(n, k):
    converted = ""

    while n > 0:
        q, r = divmod(n, k)
        converted += str(r)
        n = q

    return converted[::-1]


def get_prime(limit):
    is_prime = [True for _ in range(limit)]
    is_prime[0:2] = [False, False]
    i_limit = int(math.sqrt(limit)) + 1

    for i in range(2, i_limit):
        if is_prime[i]:
            for j in range(i + i, limit, i):
                is_prime[j] = False

    return is_prime


def get_numbers(converted):
    return re.findall("[1-9]+", converted)





n = 437674
k = 3

print(solution(n, k))


# s = re.findall(r"\d+", '12  12 drummers drumming, 11 pipers piping, 10 lords a-leaping')
# print(s)