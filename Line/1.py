import re


def solution(logs):
    return sum([is_okay(log) for log in logs])


def is_okay(log):
    if len(log) > 100:
        return 1
    pattern = r"^team_name : [a-zA-Z]+ application_name : [a-zA-Z]+ error_level : [a-zA-Z]+ message : [a-zA-Z]+$"
    return re.match(pattern, log) is None


logs = ["team_name : MyTeam application_name : YourApp error_level : info messag : IndexOutOfRange", "no such file or directory", "team_name : recommend application_name : recommend error_level : info message : RecommendSucces11", "team_name : recommend application_name : recommend error_level : info message : Success!", "   team_name : db application_name : dbtest error_level : info message : test", "team_name     : db application_name : dbtest error_level : info message : test", "team_name : TeamTest application_name : TestApplication error_level : info message : ThereIsNoError"]
print(solution(logs))