N = int(input())

A = [True for i in range(N+1)]
primes = []

for i in range(2, N+1):
    if A[i]:
        primes.append(i)
        for j in range(2 * i, N+1, i):
            A[j] = False

d = len(primes)
left = 0
right = 0
now_sum = 0
cnt = 0
while left <= right <= d:
    if now_sum >= N:
        if now_sum == N:
            cnt += 1
        now_sum -= primes[left]
        left += 1
    else:
        if right == d:
            break
        now_sum += primes[right]
        right += 1

print(cnt)