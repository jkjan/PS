
a = list(map(int, input().split()))
b = list(map(int, input().split()))
k = int(input())

c = []


for i in range(len(a)):
    for j in range(len(a)):
        c.append(a[i] + b[j])

c = list(set(c))
c.sort()

print(c[k-1])