import json

import requests


base_url = "https://kox947ka1a.execute-api.ap-northeast-2.amazonaws.com/prod/users"
x_auth_token = "c4689530a8965f7c126bc47707272239"
auth_key = ""


def get_all_history(scenario):
    return [get_history(scenario, day) for day in range(1, 4)]


def get_history(scenario, day):
    url = "https://grepp-cloudfront.s3.ap-northeast-2.amazonaws.com/programmers_imgs/competition-imgs/2021kakao/" \
          + ("problem%d_day-%d.json" % (scenario, day))
    response = requests.get(url)
    return response.json()



def start(scenario):
    global auth_key
    response = requests.post(base_url + "/start",
                             headers={
                                 "X-Auth-Token": x_auth_token,
                             },
                             data={
                                 "problem": scenario
                             }
                             )
    ret = response.json()
    auth_key = ret["auth_key"]
    return ret["time"]


def locations():
    response = requests.get(base_url + "/locations",
                            headers={
                                "Authorization": auth_key
                            }
                            )
    return response.json()["locations"]


def trucks():
    response = requests.get(base_url + "/trucks",
                            headers={
                                "Authorization": auth_key
                            }
                            )
    return response.json()["trucks"]


def simulate(commands):
    data = {"commands": commands}
    json_val = json.dumps(data)

    response = requests.put(base_url + "/simulate",
                            headers={
                                "Authorization": auth_key
                            },
                            data=json_val
                            )

    return response.json()


def score():
    response = requests.get(base_url + "/score",
                            headers={
                                "Authorization": auth_key
                            }
                            )
    return response.json()["score"]
