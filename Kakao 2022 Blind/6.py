def solution(board, skill):

    for s in skill:
        [skill_type, r1, c1, r2, c2, degree] = s
        for i in range(r1, r2 + 1):
            for j in range(c1, c2 + 1):
                if skill_type == 2:
                    board[i][j] += degree
                else:
                    board[i][j] -= degree

    cnt = 0
    for b_r in board:
        for b_c in b_r:
            if b_c >= 1:
                cnt += 1

    return cnt

