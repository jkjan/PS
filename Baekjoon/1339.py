import sys


N = int(sys.stdin.readline().strip())
alpha_to_num = [[0, 0] for i in range(26)]
words = ['' for i in range(N)]
nums = [0 for i in range(N)]

for i in range(N):
    words[i] = sys.stdin.readline().strip()

j = -1
flag = True
while flag:
    flag = False
    for i in range(N):
        if abs(j) > len(words[i]):
            continue
        flag = True
        alpha_to_num[ord(words[i][j]) - 65][0] += pow(10, abs(j) - 1)
    j -= 1

alpha_to_num.sort(key=lambda x: -x[0])

n = 0
for i in range(10):
    if alpha_to_num[i][0] == 0:
        break
    n += alpha_to_num[i][0] * (9 - i)

sys.stdout.write(str(n))