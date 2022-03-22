import sys


N = int(sys.stdin.readline().strip())

roads = list(map(int, sys.stdin.readline().split()))
cities = list(map(int, sys.stdin.readline().split()))

i = 0
cost = 0
while i < len(roads):
    j = i + 1
    gas_needed = 0
    while j < len(cities):
        gas_needed += roads[j - 1]
        if cities[i] > cities[j]:
            break
        j += 1
    cost += gas_needed * cities[i]
    i = j

sys.stdout.write(str(cost))