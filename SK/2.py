def solution(n, clockwise):
    deltas = [(0,1), (1,0), (0, -1), (-1, 0)]
    d_s = 0 if clockwise else 2
    e_s = 0 if clockwise else 1

    clockwise = 1 if clockwise else -1
    entry = [(0,0), (0, n-1),(n-1, n-1) ,(n-1, 0) ]
    vector = []
    answer = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(4):
        vector.append((entry[e_s], d_s))
        e_s = (e_s + clockwise) % 4
        d_s = (d_s + clockwise) % 4

    for ey, ex in entry:
        answer[ey][ex] = 1

    num = 2
    flag = False

    while not flag:
        for i in range(4):
            (vy, vx), d = vector[i]

            dy, dx = deltas[d]
            new_vy, new_vx = vy + dy, vx + dx

            if answer[new_vy][new_vx] != 0:
                d = (d + clockwise) % 4

            dy, dx = deltas[d]
            new_vy, new_vx = vy + dy, vx + dx

            if answer[new_vy][new_vx] != 0:
                flag = True
                break

            answer[new_vy][new_vx] = num

            vector[i] = ((new_vy, new_vx), d)


        num += 1


    return answer


n = 5
clockwise = True
