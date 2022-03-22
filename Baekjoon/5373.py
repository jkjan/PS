# 큐브 면 색깔
colors = ['w', 'y', 'r', 'o', 'g', 'b']

# 큐브 면
U, D, F, B, L, R = 0, 1, 2, 3, 4, 5

# 각 면에서 상하좌우, 왼쪽에서 오른쪽까지. [면, 시작i, 시작j, dy, dx]
cube_dirs = [
    [[B, 0, 2, 0, -1], [R, 0, 2, 0, -1], [F, 0, 2, 0, -1], [L, 0, 2, 0, -1]],
    [[F, 2, 0, 0, 1], [R, 2, 0, 0, 1], [B, 2, 0, 0, 1], [L, 2, 0, 0, 1]],
    [[U, 2, 0, 0, 1], [R, 0, 0, 1, 0], [D, 0, 2, 0, -1], [L, 2, 2, -1, 0]],
    [[U, 0, 2, 0, -1], [L, 0, 0, 1, 0], [D, 2, 0, 0, 1], [R, 2, 2, -1, 0]],
    [[U, 0, 0, 1, 0], [F, 0, 0, 1, 0], [D, 0, 0, 1, 0], [B, 2, 2, -1, 0]],
    [[U, 2, 2, -1, 0], [B, 0, 0, 1, 0], [D, 2, 2, -1, 0], [F, 2, 2, -1, 0]]
]

# 시계방향은 한 번 돌리고 반시계는 세 번 돌림
rotate_dir = {
    '+': 1,
    '-': 3
}


def solution():
    T = int(input())
    for t in range(T):
        tc()


def tc():
    cube = init_cube()
    n = int(input())
    commands = list(input().split())

    for c in commands:
        rotate(cube, eval(c[0]), rotate_dir[c[1]])

    print_cube(cube, U)


# 큐브 초기화
def init_cube():
    return [[[colors[c] for _ in range(3)] for _ in range(3)] for c in range(6)]


# 큐브 회전
def rotate(cube, face, n_rotate):
    for n in range(n_rotate):
        rotate_face(cube, face)
        rotate_sides(cube, face)


# 위에서 보는 면 회전
def rotate_face(cube, face):
    rotated = [[0 for _ in range(3)] for _ in range(3)]

    for i in range(3):
        for j in range(3):
            rotated[j][2-i] = cube[face][i][j]

    for i in range(3):
        for j in range(3):
            cube[face][i][j] = rotated[i][j]


# 사이드 회전
def rotate_sides(cube, face):
    # 3개짜리 백업하는 임시 큐브
    temp_cube = [[[0, 0, 0]]]

    # 임시 큐브를 옮기는 방향
    temp_dir = [0, 0, 0, 0, 1]

    # 처음, 끝, 인덱스 변화량
    first, last, d_dirs = 3, 0, -1

    # 끝에 부분 백업
    copy_line(temp_cube, temp_dir, cube, cube_dirs[face][first])

    # 뒤에서 앞으로 옮김
    for d in range(first, last, d_dirs):
        copy_line(cube, cube_dirs[face][d], cube, cube_dirs[face][d + d_dirs])

    # 백업했던 부분 시작으로 복원
    copy_line(cube, cube_dirs[face][last], temp_cube, temp_dir)


def copy_line(cube_dest, dest, cube_src, src):
    [d_face, d_i, d_j, d_dy, d_dx] = dest
    [s_face, s_i, s_j, s_dy, s_dx] = src

    # 각각 dy, dx 로 변화해가며 d_i, d_j 에 s_i, s_j 복사
    for n in range(3):
        cube_dest[d_face][d_i][d_j] = cube_src[s_face][s_i][s_j]
        d_i, d_j = d_i + d_dy, d_j + d_dx
        s_i, s_j = s_i + s_dy, s_j + s_dx


# 큐브 출력
def print_cube(cube, face):
    for i in range(3):
        for j in range(3):
            print(cube[face][i][j], end='')
        print()


solution()