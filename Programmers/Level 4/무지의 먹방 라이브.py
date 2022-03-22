"""
싸이클의 크기를 최대화 해서 k값을 줄여나가다가
마지막 순간에만 배열을 돌아야 하는 문제입니다.
음식의 양을 카운트하고 이를 양의 오름차순으로 정렬합니다.
정렬한 후 카운팅 된 수만큼 (음식의 양을 키로 하여) 돌면서
그 음식이 모두 비워지게 되는 싸이클의 크기를 구합니다. (to_remove)
줄여나가다가 k값이 음수가 되게 되는 싸이클에선
음식을 모두 비우는 게 아닌 하나씩 먹는 싸이클로 다시 줄입니다.
남아있는 음식의 양만큼 나누고, 나머지만 일일히 세주면 끝입니다.
"""


from collections import Counter
from math import ceil


def solution(food_times, k):
    n = len(food_times)

    # food_cnt[i] = (i 번째로 적은 음식의 양, 같은 양을 가지는 음식의 개수)
    food_cnt = sorted(list(Counter(food_times).items()))

    # 현재 먹은 각 음식의 양
    food_ate = 0

    # 남은 음식 수
    food_left = n

    for i in range(len(food_cnt)):
        # i 번째로 적은 음식의 현재 잔량
        to_eat = food_cnt[i][0] - food_ate

        # i 번째로 적은 음식을 아예 비워버리기 위해 지나야 하는 시간
        to_remove = to_eat * food_left

        # 아예 비우진 못한다면
        if k - to_remove < 0:
            # 현재 남아있는 음식들을 돌 수 있는 바퀴 수 = 더 비울 수 있는 각각의 음식의 양
            able = ceil(k / food_left)

            # able 바퀴 씩 돌고 남은 k
            k %= food_left

            # 현재 다 먹은 각 음식의 양
            now_eaten = food_ate + able

            for l in range(n):
                # 음식의 양이 현재 먹은 양보다 크거나 같다면 (= 아직 남아있다면)
                if food_times[l] >= now_eaten:
                    # k 초 후 먹을 음식 발견
                    if k == 0:
                        return l + 1
                    k -= 1

        # i 번째로 적은 음식을 아예 비워버림
        k -= to_remove

        # 지금까지 먹은 각 음식의 양 추가
        food_ate += to_eat

        # 남은 음식 개수 줄이기
        food_left -= food_cnt[i][1]

    return -1


food_times = [1, 3, 6]
k = 5
print(solution(food_times, k))