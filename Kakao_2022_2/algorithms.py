from collections import deque
import parameters as pt
import utils as ut


# 관건 1-A: 무지성으로 옆사람이랑 짝 지어주기
def get_next_user(waiting_queue, user_id, grades, matched):
    if len(waiting_queue) > 0:
        next_user = waiting_queue.popleft()
        matched.add(next_user)
        return next_user
    else:
        return -1


# 관건 1-B: 등급 차가 제일 큰 사람이랑 짝 지어주기
def get_nearest_user(waiting_queue, user_id, grades, matched):
    """
    :param waiting_queue: 대기열 (1, 2, 4, 10...)
    :param user_id: 짝 지을 유저
    :param grades: 등급
    :param matched: 매칭된 유저의 set
    :return: user_id 랑 짝 지어줄 유저
    """
    max_abs = -1
    nearest_user = -1

    # 실수: 큐를 for 문으로 참조함
    for partner in waiting_queue:
        # 파트너가 자기 자신이거나 이미 다른 유저랑 매칭이 됨
        if partner in matched or partner == user_id:
            continue
        new_abs = abs(grades[user_id] - grades[partner])

        if max_abs < new_abs:
            max_abs = new_abs
            nearest_user = partner

    matched.add(nearest_user)

    return nearest_user


# 관건 2-A: 레벨 차이를 최소-최대 정규화
# 이 정규화를 거치면 어떤 값이든 변환할 데이터의 최소값 ~ 최대값 사이로 나옴
# 여기선 레벨 차이를 등급으로 변환할 것이므로 등급의 최소에서 최대 사이의 값으로 변환됨
def min_max_normalize(x):
    return int(((x - pt.LEVEL_MIN) / (pt.LEVEL_MAX - pt.LEVEL_MIN)) * pt.GRADE_MAX)


# 관건 2-B: 레벨 차이를 z-점수 정규화
# 문제에서 레벨의 평균이랑 표준편차를 줬음
# 아마 이걸 활용하려면 이 방법 밖에 없을 듯함.
# 일단 등급의 평균을 5000으로, 표준편차를 2500으로 잡고  (0 ~ 9999 라는 범위에서 대충...)
# 이대로 계산함 (등급 평균이 레벨 평균(=40000)의 1/8이니 z_score 도 8로 나누면 되지 않을까? 라는 정신나간 생각을 함)
# 사실은 레벨의 z-score 로 등급의 z-score 는 알아낼 수 없음
def z_score_normalize(x):
    z_score = (x - pt.LEVEL_MEAN) / pt.LEVEL_STD
    return int(min(max(pt.GRADE_MIN, 5000 + 2500 * (z_score / 8)), pt.GRADE_MAX))


# 관건 3-A: 등급 차를 반으로 나누어서 승자한테는 반을 더하고 패자한테는 반을 더함
def add_and_subtract_half(winner_grade, loser_grade, grade_diff):
    half = grade_diff // 2
    # 단 등급은 최대 9999를 넘을 수 없고 0보다 작아질 수 없으므로, min 과 max 을 적용함
    return min(winner_grade + half, 9999), max(loser_grade - half, 0)


# 관건 3-B: 등급 차를 승자한테 다 더해줌
def add_all_to_winner(winner_grade, loser_grade, grade_diff):
    return min(winner_grade + grade_diff, 9999), loser_grade


# 관건 4: 패자가 어뷰저임이 적발되면 둘의 등급을 스왑 (승자 등급 <- 패자 등급 , 패자 등급 <- 승자 등급)
def swap_when_abused(winner_grade, loser_grade, grade_diff):
    return loser_grade, winner_grade


# 게임 결과랑 어뷰징 확률로 등급을 갱신할 유저의 리스트 반환
def naive_grade_changing(results, grades, abuse_rate, methods):
    """
    :param results: 게임 결과
    :param grades: 유저별 등급 -> {id: grade}
    :param abuse_rate: 유저별 어뷰징 확률
    :param methods: 이용할 메소드들
    :return: 새로 갱신할 유저의 등급
    """
    to_change = []

    for result in results:
        # 걸린 시간에서 레벨 차이를 추정
        level_diff = ut.get_approx_level_diff(result["taken"])

        # 승자와 패자의 현재 등급을 가져옴
        winner_grade = grades[result["win"]]
        loser_grade = grades[result["lose"]]

        # 레벨 차이를 등급 차이로 변환함
        grade_diff = methods["normalize"](level_diff)
        loser_id = result["lose"]

        # 2번 문제인데 패자가 어뷰저임이 적발되면
        if pt.PROBLEM == 2 and abuse_rate[loser_id][1] != 0 and ut.get_probability(abuse_rate[loser_id]) >= 0.8:
            # 승자와 패자 등급을 어뷰저 로직대로 계산함
            new_winner_grade, new_loser_grade = methods["method_for_abuser"](winner_grade, loser_grade, grade_diff)
        else:
            # 아니면 일반적인 등급 반환 로직대로 계산함
            new_winner_grade, new_loser_grade = methods["method_for_grade_revise"](winner_grade, loser_grade, grade_diff)

        # 새로 바뀐 승자와 패자의 등급을 추가함
        to_change += [
            {"id": result["win"], "grade": new_winner_grade},
            {"id": result["lose"], "grade": new_loser_grade}
        ]

    return to_change


def make_pairs(waiting_line, grades, methods):
    """
    :param waiting_line: 카카오에서 준 대기열 -> [{"from": 들어온 시간, "id": 유저 아이디},...]
    :param grades: 유저별 등급 -> {id: grade}
    :param methods: 사용할 메소드들
    :return: 싸움 붙일 순서쌍
    """

    # 대기열을 들어온 시간 순서대로 정렬함
    waiting_queue = get_waiting_queue(waiting_line)
    matched = set()
    to_pair = []

    while len(waiting_queue) > 0:
        user_id = waiting_queue.popleft()

        # user_id 랑 싸움 붙일 놈을 고름
        get_partner = methods["pick_partner"](waiting_queue, user_id, grades, matched)

        # 붙일 놈이 있을 경우
        if get_partner != -1:
            to_pair.append(sorted([user_id, get_partner]))
            matched.add(user_id)

    return to_pair


def get_waiting_queue(waiting_line):
    """
    :param waiting_line: 대기열 -> [{"from": 들어온 시간, "id": 유저 아이디},...]
    :return: 유저 아이디 값만 들어간 큐 (온 순으로 정렬된)
    """
    waiting_queue = deque()
    waiting_line = sorted(waiting_line, key=lambda x: x["from"])

    while len(waiting_line) > 0:
        waiting_queue.append(waiting_line.pop()["id"])

    return waiting_queue


def get_rate(results, grades, abuse_rate):
    """
    :param results: 게임 결과
    :param grades: 유저별 등급 -> {id: grade}
    :param abuse_rate: 어뷰징 확률
    """
    for result in results:
        winner_id = result["win"]
        loser_id = result["lose"]

        # 이거 확률 계산이 잘못됐음
        if grades[winner_id] < grades[loser_id] and result["taken"] <= 10:
            abuse_rate[loser_id][0] += 1

        abuse_rate[loser_id][1] += 1
        abuse_rate[winner_id][1] += 1


        # 원래는 이거여야 함. 아마 여기서 질문 들어올 듯
        if grades[winner_id] < grades[loser_id]:
            if result["taken"] <= 10:
                abuse_rate[loser_id][0] += 1
            abuse_rate[loser_id][1] += 1
