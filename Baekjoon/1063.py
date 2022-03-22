LIMIT = 8

deltas = {
    'R': (0, 1),
    'L': (0, -1),
    'B': (1, 0),
    'T': (-1, 0)
}


def solution():
    king, stone, commands = get_input()
    king = chess_notation_to_ij(king)
    stone = chess_notation_to_ij(stone)

    for c in commands:
        moved_king = move(king, c)
        moved_stone = stone

        if moved_king == stone:
            moved_stone = move(stone, c)

        if is_valid(*moved_king) and is_valid(*moved_stone):
            king = moved_king
            stone = moved_stone

    print(ij_to_chess_notation(*king))
    print(ij_to_chess_notation(*stone))


def move(horse, command):
    horse_y, horse_x = horse

    for c in command:
        dy, dx = deltas[c]
        horse_y += dy
        horse_x += dx

    return horse_y, horse_x


def is_valid(i, j):
    return 0 <= i < LIMIT and 0 <= j < LIMIT


def get_input():
    king, stone, N = input().split()
    N = int(N)
    commands = [input() for _ in range(N)]
    return king, stone, commands


def chess_notation_to_ij(notation):
    i = LIMIT - int(notation[1])
    j = ord(notation[0]) - ord('A')
    return i, j


def ij_to_chess_notation(i, j):
    return chr(ord('A') + j) + str(LIMIT - i)


solution()