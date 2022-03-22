from collections import deque, defaultdict
from copy import deepcopy


def solution(tickets):
    graph, ticket_dict = make_graph(tickets)
    will_visit = deque([("ICN", deepcopy(ticket_dict), ["ICN"])])

    while len(will_visit) > 0:
        now_airport, tickets_left, now_path = will_visit.popleft()
        if len(tickets_left) == 0:
            return now_path

        for adj in graph[now_airport]:
            line = (now_airport, adj)
            if line in tickets_left.keys() and tickets_left[line] > 0:
                next_tickets = deepcopy(tickets_left)
                next_tickets[line] -= 1
                if next_tickets[line] == 0:
                    next_tickets.pop(line)
                will_visit.append((adj, next_tickets, now_path + [adj]))


def make_graph(tickets):
    graph = defaultdict(lambda : [])
    ticket_dict = defaultdict(lambda : 0)

    for from_, _to in tickets:
        graph[from_].append(_to)
        ticket_dict[(from_, _to)] += 1

    for from_ in graph.keys():
        graph[from_].sort()

    return graph, ticket_dict


tickets =[["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]

print(solution(tickets))