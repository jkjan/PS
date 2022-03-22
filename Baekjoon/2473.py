import math
import sys


def solution():
    # 입력
    N, arr = get_input()

    # 정렬
    arr.sort()

    # 최소값 초기화
    min_diff = math.inf
    answer = (0, 0, 0)

    # 한 인덱스를 i로 고정한다.
    for i in range(N - 2):
        # 나머지 부분의 시작과 끝 인덱스
        s = i + 1
        e = N - 1
        target = -arr[i]

        # s < e 인 동안 arr[s] + arr[e]가 -target 과 최대한 가까워지는 s와 e를 찾는다.
        while s < e:
            res = arr[s] + arr[e]
            now_diff = abs(res + arr[i])

            # 그 과정에서 보는 모든 경우에 대해서 항상 합의 절대값이 최소가 되는 세 수를 갱신한다.
            if min_diff > now_diff:
                min_diff = now_diff
                answer = arr[i], arr[s], arr[e]

            # 두 수의 합이 target 보다 작으면 s를 증가시킨다. 정렬되어 있기 때문에 s를 증가시키면 큰 수가 나온다.
            # 크면 e를 증가시킨다. 정렬되어 있기 때문에 e를 줄이면 작은 수가 나온다.
            if res < target:
                s += 1
            elif res > target:
                e -= 1
            else:
                # 두 수의 합이 target 과 같으면 이미 그 수의 합이 0이 됐다는 뜻이다.
                # 스페셜 저지이므로 바로 출력해줘도 무방하다.
                return arr[i], arr[s], arr[e]

    # 합의 절대값이 최소가 되는 세 수의 조합을 리턴한다.
    # 여기까지 왔다면 절대 0은 안 나온다는 말이다.
    return answer


def get_input():
    N = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    return N, arr


sys.stdout.write("%d %d %d" % solution())