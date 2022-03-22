import heapq
from collections import deque

READ = 1
WRITE = 0

def solution(arr, processes):
    ready_queue = []
    now_processes = []
    used_time = 0


    read_cnt = -1
    for i in range(len(processes)):
        p = processes[i].split(" ")
        if p[0] == "read":
            p[0] = '1'
            read_cnt += 1
        else:
            p[0] = '0'
        p = list(map(int, p))
        processes[i] = p + [read_cnt]

    answer = ["" for _ in range(read_cnt + 1)]

    i = 0
    t = -1
    while True:
        t += 1
        used_time += len(now_processes) >= 1
        # print(t, i)
        # print(now_processes)

        # 끝난 프로세스 제거
        while now_processes:
            if now_processes[0][0] == t:
                terminate = heapq.heappop(now_processes)
                if terminate[-1] == READ:
                    # print("읽기 끝", terminate[3], terminate[4])
                    answer[terminate[-2]] = ("".join(arr[terminate[3]:terminate[4] + 1]))
                else:
                    # print("쓰기 끝", terminate[3], terminate[4], terminate[5])
                    for k in range(terminate[3], terminate[4] + 1):
                        arr[k] = str(terminate[5])
            else:
                break

        if i >= len(processes):
            if len(now_processes) >= 1:
                continue
            if len(ready_queue) == 0:
                break
        else:
            if t < processes[i][1] and len(ready_queue) == 0:
                # print("아직 수행할 프로세스가 도착하지 않았으며 대기하고 있는 프로세스도 없음")
                continue
            elif t == processes[i][1]:
                # print("실행할 프로세스 도착 -> 대기 큐에 넣음")
                heapq.heappush(ready_queue, processes[i])
                i += 1

        # 쓰기 프로세스가 진행 중임
        if len(now_processes) == 1 and now_processes[0][-1] == WRITE:
            # print("쓰기 프로세스 진행 중")
            continue

        # 읽기 프로세스가 진행 중임
        if len(now_processes) >= 1 and now_processes[0][-1] == READ:
            if ready_queue[0][0] == WRITE:
                # print("읽기 프로세스가 진행 중인데 대기열에 쓰기 있음")
                continue

        while ready_queue:
            to_execute = heapq.heappop(ready_queue)
            # print(to_execute, "시작")
            expire = [t + to_execute[2]] + to_execute[1:] + [to_execute[0]]
            heapq.heappush(now_processes, expire)
            if to_execute[0] == WRITE:
                break

    answer.append(str(used_time))
    return answer


arr = ["1","2","4","3","3","4","1","5"]
processes = ["read 1 3 1 2","read 2 6 4 7","write 4 3 3 5 2","read 5 2 2 5","write 6 1 3 3 9", "read 9 1 0 7"]
# print(solution(arr, processes))