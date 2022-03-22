def get_results():
    output_file_name = "line_output.txt"
    output_file = open(output_file_name, "rt")
    output_list = output_file.read().splitlines()
    output_list = list(map(int, output_list))
    return output_list


def get_arr():
    input_file_name = "line_input.txt"
    input_file = open(input_file_name, "rt")
    input_list = input_file.read().splitlines()
    input_list = list(map(lambda x: list(map(int, x.split())), input_list))
    return input_list


def solve():
    arrs = get_arr()
    results = get_results()

    for i in range(len(arrs)):
        answer = solution(arrs[i])
        result = results[i]
        print("CORRECT" if answer == result else "WRONG")


def solution(arr):
    FLAT = 0  # 평평함 (처음에는 평평)
    ASCENDING = 1 # 올라가는 중
    DESCENDING = 2 # 내려가는 중

    s = 0
    cnt = 0
    peak = -1
    status = FLAT

    for i in range(1, len(arr)):
        if arr[i-1] < arr[i]:  # 올라감
            if status != ASCENDING: # 처음 올라가는 거면 s, peak 초기화
                s = i - 1
                peak = -1
            status = ASCENDING

        elif arr[i-1] == arr[i]: # 평평함
            # s, peak 초기화
            s = i
            peak = -1
            status = FLAT

        else: # 내려감
            if status == FLAT:
                # 처음 내려가는 거면 s, peak 초기화
                s = i
                peak = -1
            else:
                # 올라갔다가 내려온 거면 피크 설정
                if status == ASCENDING:
                    peak = i - 1

                # 이전에 피크가 설정돼있었다면 A 배열의 일부이므로 전체 개수 올림
                if peak != -1:
                    cnt += peak - s

            status = DESCENDING

    return cnt


solve()