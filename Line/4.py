def solution(arr, brr):
    answer = 0
    for i in range(len(arr) - 1):
        if arr[i] != brr[i]:
            arr[i + 1] -= brr[i] - arr[i]
            arr[i] = brr[i]
            answer += 1
    return answer