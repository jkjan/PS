def solution(num_teams, remote_tasks, office_tasks, employees):
    teams = [[] for _ in range(num_teams + 1)]
    remote_tasks = set(remote_tasks)
    salesmen = [0 for _ in range(len(employees) + 1)]
    office_tasks = set(office_tasks)
    go_to_work = [[] for _ in range(num_teams + 1)]

    for i, employee in enumerate(employees):
        i = i + 1
        e = employee.split()
        team_number, task_list = e[0], e[1:]
        team_number = int(team_number)
        teams[team_number].append(i)

        for task in task_list:
            if task in office_tasks:
                go_to_work[team_number].append(i)

    for i in range(1, num_teams + 1):
        if len(go_to_work[i]) == 0:
            teams[i].sort()
            go_to_work[i].append(teams[i][0])

        for j in go_to_work[i]:
            salesmen[j] = 1

    answer = [i for i in range(1, len(employees) + 1) if salesmen[i] == 0]
    answer.sort()

    return answer