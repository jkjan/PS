import json

import requests
import parameters as pt


auth_key = "5af30a60-086c-45de-a8d4-303d1ad5b20e"
base_url = "https://huqeyhi95c.execute-api.ap-northeast-2.amazonaws.com/prod"
x_auth_token = "9d4fb3b5d76ad2d445af1d46223b663a"


def start():
    global auth_key
    response = requests.post(url=base_url + "/start",
                  headers={
                      "X-Auth-Token": x_auth_token,
                  },
                  data={
                      "problem": pt.PROBLEM
                  })
    ret = response.json()
    print(ret)
    auth_key = ret["auth_key"]
    pt.PROBLEM = ret["problem"]

    return ret


def get_waiting_line():
    response = requests.get(url=base_url + "/waiting_line",
                            headers={
                                "Authorization": auth_key
                            })
    return response.json()["waiting_line"]


def get_game_result():
    response = requests.get(url=base_url + "/game_result",
                            headers={
                                "Authorization": auth_key,
                            })
    return response.json()["game_result"]


def get_user_info():
    response = requests.get(url=base_url + "/user_info",
                            headers={
                                "Authorization": auth_key,
                            })
    return response.json()["user_info"]


def match(pairs):
    response = requests.put(url=base_url + "/match",
                            headers={
                                "Authorization": auth_key,
                            },
                            data=json.dumps(pairs)
                            )
    return response.json()


def change_grade(commands):
    response = requests.put(url=base_url + "/change_grade",
                            headers={
                                "Authorization": auth_key,
                            },
                            data=json.dumps(commands)
                            )
    return response.json()


def score():
    response = requests.get(base_url + "/score",
                            headers={
                                "Authorization": auth_key
                            }
                            )
    return response.json()
