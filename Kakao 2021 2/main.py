from collections import deque, defaultdict
import utils as ut
import parameters as pt
import api_utils as au
import algorithms as ag


ut.select_scenario(pt.scenario)
time = au.start(pt.scenario)
history = au.get_all_history(pt.scenario)
hot_places = ut.get_n_hot_places(history, pt.TRUCKS)
ut.init_rental()
truck_queue = defaultdict(lambda: deque())


while time < pt.MAX_TIME:
    locations_info = au.locations()
    trucks_info = au.trucks()
    ut.renew_rental(locations_info)
    pattern = time // pt.PATTERN_INTERVAL
    visited = [False for _ in range(pt.N * pt.N)]
    commands = []

    for truck_info in trucks_info:
        command = ag.get_command(truck_info, hot_places, pattern, visited, time, truck_queue)
        commands.append({"truck_id": truck_info["id"], "command": command})

    result = au.simulate(commands)
    print(result)
    time = result["time"]


s = au.score()
print(s)