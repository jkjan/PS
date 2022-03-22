MAX = 1_000_001


def solution(rectangles):
    rectangles = [(i, rectangles[i]) for i in range(len(rectangles))]
    drag(rectangles, 0, 2, 1, 3)
    drag(rectangles, 1, 3, 0, 2)
    rectangles.sort(key=lambda x: x[0])
    answer = [" ".join(list(map(lambda x: str(x), y[1]))) for y in rectangles]
    return answer


def drag(rectangles, a, b, c, d):
    # 직사각형 정렬
    rectangles.sort(key=lambda x: x[1][c])

    # 바닥에서 가장 높은 부분
    top = [0 for _ in range(MAX)]

    for r in range(len(rectangles)):
        # 직사각형의 양쪽 끝단 인덱스
        s = rectangles[r][1][a]
        e = rectangles[r][1][b]

        # 양쪽 끝 구간에서 가장 큰 높이
        till = max(top[s:e])

        # 직사각형 밑부분에서 최대로 내릴 수 있는 부분까지의 거리
        dist = rectangles[r][1][c] - till

        # 직사각형을 내림
        rectangles[r][1][c] -= dist
        rectangles[r][1][d] -= dist

        # 직사각형의 높이
        height = rectangles[r][1][d] - rectangles[r][1][c]

        # 최대 높이 변경
        for t in range(s, e):
            top[t] = till + height


rectangles = [[0,2,1,3], [1,2,2,5], [3,3,4,4], [4,1,6,3], [1,6,5,7],[5,5,7,6], [5,8,6,10]]
answer = solution(rectangles)
print(answer)