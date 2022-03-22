import utils as ut
import parameters as pt
from collections import deque


def get_command(truck_info, hot_places, pattern, visited, time, truck_queue):
    truck_pos = truck_info["location_id"]
    pick_up = ut.find_nearest_spot(truck_pos, hot_places, pattern, pt.RETURN, visited)
    put = ut.find_nearest_spot(truck_pos, hot_places, pattern, pt.RENT, visited)

    queue = deque(ut.add_to_truck_command_queue(truck_pos, pick_up, put))

    if (time + (((len(truck_queue[truck_info["id"]]) + len(queue)) * 6) // 60)) // pt.PATTERN_INTERVAL == pattern:
        while len(queue) > 0:
            truck_queue[truck_info["id"]].append(queue.popleft())

        command = []

        for i in range(10):
            if len(truck_queue[truck_info["id"]]) > 0:
                command.append(truck_queue[truck_info["id"]].popleft())
            else:
                command.append(0)

    else:
        command = [0 for _ in range(10)]

    return command
