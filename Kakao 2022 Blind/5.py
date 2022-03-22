from copy import deepcopy


def solution(info, edges):
    tree = [[] for _ in range(len(info))]
    blocked = []
    max_sheep = 0

    def make_tree():
        for parent, child in edges:
            tree[parent].append(child)


    def dfs(node, sheep, wolves):
        nonlocal max_sheep
        print(node, sheep, wolves)
        if info[node] == 0:
            sheep.add(node)

            if len(blocked) > 0:
                [blocked_node, blocked_sheep, blocked_wolves] = blocked[-1]
                if_go_sheep = blocked_sheep.union(sheep)
                if_go_wolves = blocked_wolves.union(wolves)
                if len(if_go_sheep) > len(blocked_wolves.union(if_go_wolves)):
                    dfs(blocked_node, deepcopy(if_go_sheep), deepcopy(if_go_wolves))

            max_sheep = max(max_sheep, len(sheep))
        else:
            wolves.add(node)

        able = False
        for child in tree[node]:
            print(child, sheep, wolves)
            if info[child] == 0 or (info[child] == 1 and len(wolves) + 1 < len(sheep)):
                print(child)
                able = True
                dfs(child, deepcopy(sheep), deepcopy(wolves))

        if len(tree[node]) > 0 and not able:
            blocked.append([node, sheep, wolves])

    make_tree()
    dfs(0, set(), set())
    return max_sheep


info = [0,0,1,1,1,0,1,0,1,0,1,1]

edges = [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]

print(solution(info, edges))