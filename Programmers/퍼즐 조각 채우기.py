from collections import deque, defaultdict


# 게임 보드와 테이블의 행, 열 길이
N = 0

# 위치 이동 변화량
deltas = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def solution(game_board, table):
    global N
    N = len(game_board)

    # 게임 보드의 빈칸들
    blanks = get_all_groups(game_board, 0)

    # 테이블의 퍼즐 조각들
    puzzle_pieces = get_all_groups(table, 1)

    piece_ids_by_length = get_piece_ids_by_length(blanks, puzzle_pieces)

    # 총 채워진 빈칸 수
    answer = fill_blanks(blanks, piece_ids_by_length, puzzle_pieces)

    return answer


def get_piece_ids_by_length(blanks, puzzle_pieces):
    """
    :param blanks: 빈칸들
    :param puzzle_pieces: 퍼즐 조각들
    :return: {빈칸의 크기: [크기가 똑같은 퍼즐 조각의 id]}
    """
    # 빈칸 크기들 집합
    length_set = set([len(x) for x in blanks])

    piece_ids_by_length = defaultdict(lambda: [])

    # 퍼즐 조각의 크기 별로 id를 리스트에 추가
    for i, pp in enumerate(puzzle_pieces):
        if len(pp) in length_set:
            piece_ids_by_length[len(pp)].append(i)

    return piece_ids_by_length


def get_all_groups(field, to_group):
    """
    :param field: N * N 의 이차원 배열 (게임 보드 혹은 테이블)
    :param to_group: 그룹 지을 수
    :return: to_group 으로 이어진 그룹들의 리스트
    """
    visited = [[False for _ in range(N)] for _ in range(N)]
    groups = []

    for i in range(N):
        for j in range(N):
            if field[i][j] == to_group and not visited[i][j]:
                visited[i][j] = True
                group = bfs((i, j), visited, field, to_group)
                groups.append(group)

    return groups


def bfs(start, visited, field, to_group):
    """
    :param start: (시작 y, 시작 x)
    :param visited: 방문 여부
    :param field: N * N 의 이차원 배열 (게임 보드 혹은 테이블)
    :param to_group: 그룹 지을 키
    :return: to_group 으로 이어진 부분의 위치 리스트
    """
    will_visit = deque([start])
    group = []

    while len(will_visit) > 0:
        now_y, now_x = will_visit.popleft()

        # 그룹에 현재 위치 추가
        group.append((now_y, now_x))

        for dy, dx in deltas:
            adj_y, adj_x = now_y + dy, now_x + dx

            # 유효하지 않거나 이미 방문했거나 그룹 지을 키가 아니라면 생략
            if not is_valid(adj_y, adj_x):
                continue
            if visited[adj_y][adj_x]:
                continue
            if field[adj_y][adj_x] != to_group:
                continue

            visited[adj_y][adj_x] = True
            will_visit.append((adj_y, adj_x))

    return group


def is_valid(i, j):
    """
    :param i: y축 인덱스
    :param j: x축 인덱스
    :return: N * N 크기 2차원 배열에서 유효한 인덱스인지 여부
    """
    return 0 <= i < N and 0 <= j < N


def fill_blanks(blanks, piece_ids_by_length, puzzle_pieces):
    """
    :param blanks: 빈칸들
    :param piece_ids_by_length: {빈칸의 크기: [크기가 똑같은 퍼즐 조각의 id]}
    :param puzzle_pieces: 퍼즐 조각들
    :return: 채워진 빈칸 수
    """
    filled = 0

    # 퍼즐 조각의 사용 여부
    used = [False for _ in range(len(puzzle_pieces))]

    for blank in blanks:
        # 빈칸에 들어갈 퍼즐 조각이 있으면 그 크기만큼 채운 칸 수 증가
        if find_piece(blank, piece_ids_by_length, puzzle_pieces, used):
            filled += len(blank)

    return filled


def find_piece(blank, piece_ids_by_length, puzzle_pieces, used):
    """
    :param blank: 빈칸들
    :param piece_ids_by_length: {빈칸의 크기: [크기가 똑같은 퍼즐 조각의 id]}
    :param puzzle_pieces: 퍼즐 조각들
    :param used: 퍼즐 조각 사용 여부
    :return: 빈칸에 들어갈 퍼즐 조각이 있는지 여부
    """
    blank_size = len(blank)

    # 퍼즐 조각 후보 id = 크기가 빈칸과 같은 퍼즐 조각들
    piece_candidate_ids = piece_ids_by_length[blank_size]

    # 빈칸을 영점 기준으로 이동하고 정렬함
    blank = regularize(blank)

    for pi in piece_candidate_ids:
        # 이미 사용된 조각이라면 생략
        if used[pi]:
            continue

        # 다 똑같은 조각이므로 빈칸에 맞는 조각이 여러개더라도 어느 하나만 맞으면 됨
        # 따라서 현재 퍼즐 조각이 빈칸에 맞으면 사용 표시하고 중단
        if is_fit(blank, puzzle_pieces[pi]):
            used[pi] = True
            return True

    return False


def is_fit(blank, piece):
    """
    :param blank: 빈칸
    :param piece: 퍼즐 조각
    :return: 퍼즐 조각이 빈칸에 맞는지 여부
    """
    for i in range(4):
        # 조각을 영점 기준으로 이동하고 정렬함
        piece = regularize(piece)

        # 조각이 빈칸에 맞음
        if piece == blank:
            return True

        # 조각을 회전시킴
        piece = rotate(piece)

    return False


def regularize(group):
    """
    :param group: 그룹 (빈칸, 퍼즐 조각)
    :return: 영점 기준으로 이동되고 정렬된 그룹
    """
    # 그룹 정렬
    group_sorted = sorted(group)

    # 맨 왼쪽 상단의 y, x
    tip_y, tip_x = group_sorted[0]

    # 맨 왼쪽 상단을 (0, 0)으로 하는 기준으로 평행 이동
    group_moved = [(y - tip_y, x - tip_x) for y, x in group_sorted]

    return group_moved


def rotate(piece):
    """
    :param piece: 퍼즐 조각
    :return: 시계 방향으로 90도 회전된 퍼즐 조각
    """
    return [(y, -x) for x, y in piece]
