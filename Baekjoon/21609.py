N, M = 0, 0
rc = []
deltas = [(-1, 0), (0, 1), (1, 0), (0, -1)]
BLANK = -2


class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None


class Queue:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.right = self.tail
        self.tail.left = self.head
        self.cnt = 0


    def append(self, x):
        new_node = Node(x)
        self.tail.left.right = new_node
        new_node.left = self.tail.left
        new_node.right = self.tail
        self.tail.left = new_node
        self.cnt += 1


    def __len__(self):
        return self.cnt


    def popleft(self):
        if self.cnt == 0:
            return None

        popped = self.head.right.data
        self.head.right.right.left = self.head
        self.head.right = self.head.right.right
        self.cnt -= 1

        return popped


def solution():
    get_input()
    score = 0

    while True:
        group_size = auto_play()
        if group_size == -1:
            break
        score += group_size ** 2

    print(score)


def get_input():
    global N, M
    N, M = map(int, input().split())

    for i in range(N):
        rc.append(list(map(int, input().split())))


def bfs(i, j, visited):
    will_visit = Queue()
    will_visit.append((i, j))
    init_color = rc[i][j]
    normal_blocks = []
    rainbows = []

    while len(will_visit) > 0:
        now_y, now_x = will_visit.popleft()

        if rc[now_y][now_x] == 0:
            rainbows.append((now_y, now_x))
        else:
            normal_blocks.append((now_y, now_x))

        for dy, dx in deltas:
            adj_y, adj_x = now_y + dy, now_x + dx

            if not is_valid(adj_y, adj_x):
                continue
            if visited[adj_y][adj_x]:
                continue
            if rc[adj_y][adj_x] < 0:
                continue
            if rc[adj_y][adj_x] != 0 and init_color != rc[adj_y][adj_x]:
                continue

            visited[adj_y][adj_x] = True
            will_visit.append((adj_y, adj_x))

    for rb_y, rb_x in rainbows:
        visited[rb_y][rb_x] = False

    return normal_blocks, rainbows


def is_valid(i, j):
    return 0 <= i < N and 0 <= j < N


def get_block_group_to_erase():
    visited = [[False for _ in range(N)] for _ in range(N)]
    groups = []

    for i in range(N):
        for j in range(N):
            if not visited[i][j] and rc[i][j] > 0:
                visited[i][j] = True
                normal_blocks, rainbows = bfs(i, j, visited)
                group = normal_blocks + rainbows

                if len(group) >= 2:
                    std_y, std_x = min(normal_blocks, key=lambda x: (x[0], x[1]))
                    groups.append([len(group), len(rainbows), std_y, std_x, group])


    if len(groups) == 0:
        return None

    groups.sort(reverse=True, key=lambda x: (x[0], x[1], x[2], x[3]))

    return groups[0][4]


def erase_block_group(group):
    for b_y, b_x in group:
        rc[b_y][b_x] = BLANK


def gravity():
    for i in range(N-2, -1, -1):
        for j in range(N):
            if rc[i][j] >= 0:
                block = rc[i][j]
                rc[i][j] = BLANK

                fall_to = i + 1
                while fall_to < N and rc[fall_to][j] == BLANK:
                    fall_to += 1

                rc[fall_to - 1][j] = block


def rotate_counter_clock_wise():
    rotated_field = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            rotated_field[N - j - 1][i] = rc[i][j]

    for i in range(N):
        for j in range(N):
            rc[i][j] = rotated_field[i][j]


def auto_play():
    group = get_block_group_to_erase()

    if group is None:
        return -1

    erase_block_group(group)
    gravity()
    rotate_counter_clock_wise()
    gravity()

    return len(group)


solution()