# 표준입출력 위함
import sys


# 수를 합이 최대가 나오게 묶었을 때 합을 반환
def solution():
    # 수열을 입력 받음
    arr = get_input()

    # 절대값을 기준으로 내림차순 정렬
    arr.sort(key=lambda x: -abs(x))

    # 아무런 수도 묶지 않았을 때의 합
    answer = sum(arr)

    # 이득이 0이 될 때까지 이득을 더해나감
    while True:
        max_benefit, arr = get_max_benefit_and_excluded(arr)
        if max_benefit == 0:
            break
        answer += max_benefit

    return answer


# 입력받은 수열을 반환
def get_input():
    # N 값
    N = int(sys.stdin.readline())

    # 수열
    arr = [int(sys.stdin.readline()) for i in range(N)]

    return arr


# 최대의 이득과 그때의 수열을 반환
def get_max_benefit_and_excluded(arr):
    # 앞에서 첫번째, 두번째 양수 (없으면 None)
    first_pos_idx = get_max_value_since(arr, 0, pos=True)
    second_pos_idx = get_max_value_since(arr, first_pos_idx + 1, pos=True) if first_pos_idx is not None else None

    # 앞에서 첫번째, 두번째 음수 혹은 0 (없으면 None)
    first_neg_or_zero_idx = get_max_value_since(arr, 0, pos=False)
    second_neg_or_zero_idx = get_max_value_since(arr, first_neg_or_zero_idx + 1, pos=False) if first_neg_or_zero_idx is not None else None

    # 각각 양수, 음수와 0끼리 묶었을 때의 이득과 묶인 후의 수열
    pos_combined = get_benefit_and_excluded_when_combined(arr, first_pos_idx, second_pos_idx)
    neg_or_zero_combined = get_benefit_and_excluded_when_combined(arr, first_neg_or_zero_idx, second_neg_or_zero_idx)

    # 두 경우에서 최대의 이득과 그때의 수열을 반환
    return max(pos_combined, neg_or_zero_combined, key=lambda x: x[0])


# i부터 시작해 처음으로 등장하는 양수나 음수 혹은 0의 인덱스를 반환
def get_max_value_since(arr, i, pos):
    if pos:
        compare = lambda a, b: a > b
    else:
        compare = lambda a, b: a <= b

    while i < len(arr):
        if compare(arr[i], 0):
            return i
        i += 1

    # i부터 등장하는 양수 혹은 음수 혹은 0이 없다면 None 반환
    return None


# 양수, 음수 혹은 0끼리 묶었을 때의 이득과 묶인 수를 제거한 배열을 반환 (이득 없을 시 None)
def get_benefit_and_excluded_when_combined(arr, c1, c2):
    benefit, excluded = 0, None
    if c1 is not None and c2 is not None:
        excluded = [arr[i] for i in range(len(arr)) if i not in [c1, c2]]
        mul = arr[c1] * arr[c2]
        benefit = mul - (arr[c1] + arr[c2])
    return benefit, excluded


sys.stdout.write("%d" % solution())