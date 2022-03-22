from collections import defaultdict
import api_utils as au
import parameters as pt
import algorithms as ag
import utils as ut


methods = {
    "pick_partner": ag.get_next_user,       # 게임할 쌍 고르는 방법 (관건 1)
    "normalize": ag.min_max_normalize,      # 레벨 차이 -> 등급 변환 (관건 2)
    "method_for_grade_revise": ag.add_all_to_winner,  # 등급 차에서 유저 별 등급 (관건 3)
    "method_for_abuser": ag.swap_when_abused          # 어뷰저 처리 방법 (관건 4)
}


def solve(problem):
    """
    :param problem: 풀 문제 번호
    :return: 점수
    """

    # 파라미터 모듈의 PROBLEM 값을 바꿈
    pt.PROBLEM = problem

    # 카카오한테 내가 problem 을 풀기 시작한다고 알림
    au.start()

    t = 0

    # 각 유저가 어뷰저일 확률 -> abuse_rate[id] = [자기보다 등급 낮은 놈한테 10초 이하로 진 수 / 자기보다 등급 낮은 놈한테 진 수]
    abuse_rate = defaultdict(lambda: [0, 0])

    while t < pt.TIME_LIMIT + 1:
        print(t)

        # 카카오한테서 데이터 받아옴
        now_user_info = au.get_user_info()
        now_waiting = au.get_waiting_line()
        now_result = au.get_game_result()

        # user_info 가 [{“id”: 1, “grade”: 1}, {“id”: 2, “grade”: 100}, ...] 로 돼있어서 이걸 {1: 1, 2: 100...} 으로 탐색 편하게 바꿈
        grades = ut.user_info_to_grades(now_user_info)

        # 게임 결과대로 각 유저들의 어뷰징 확률 갱신
        ag.get_rate(now_result, grades, abuse_rate)

        # 게임 결과를 토대로 유저 등급을 수정함
        to_change = ag.naive_grade_changing(now_result, grades, abuse_rate, methods)

        # 수정한 내용을 그대로 grade 에 반영
        ut.change_grades(grades, to_change)

        # 대기열에 있는 애들을 매칭시킴
        to_pair = ag.make_pairs(now_waiting, grades, methods)

        # 카카오한테 매칭 정보와 변경할 정보를 보냄
        au.match({"pairs": to_pair})
        au.change_grade({"commands": to_change})

        t += 1

    final = au.score()
    return final


if __name__ == '__main__':
    problems = [1]
    for problem in problems:
        print(solve(problem))