from random import randint

"""
걸린 시간 = -(레벨 차이 / 99000 / 35) + e + 40, 여기서 e는 -5부터 5까지의 랜덤값
"""

# 랜덤값 생성
def generate_e():
    return randint(-5, 5)


# 걸린 시간에서 레벨 차이 알아냄 (랜덤값 때문에 정확하진 않음)
def get_approx_level_diff(taken):
    """
    :param taken: 싸움이 끝나는 데 걸린 시간
    :return: 레벨 차이의 근삿값
    """
    return -(taken - generate_e() - 40) * 99000 * 35


# 카카오가 준 정보는 {"id": ~, "grade": ~} 의 리스트로 된 정보.
# 이걸 내가 id로 grade 를 찾으려면 O(N)이므로 처음부터 그냥 {id: grade}의 딕셔너리로 변환
def user_info_to_grades(user_info):
    """
    :param user_info: 카카오가 준 유저 정보
    :return: {id: grade} 로 된 딕셔너리
    """
    grades = {}
    for info in user_info:
        grades[info["id"]] = info["grade"]
    return grades


# 새로 갱신된 등급 데이터를 다시 등급에 반영
def change_grades(grades, to_change):
    """
    :param grades: {id: grade} 로 된 딕셔너리
    :param to_change: 새로 갱신된 등급 데이터 -> [{"id": value, "grade": value}]
    """
    for c in to_change:
        grades[c["id"]] = c["grade"]


def get_probability(x):
    return x[0] / x[1]