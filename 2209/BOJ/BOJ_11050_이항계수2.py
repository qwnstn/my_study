n, k = map(int, input().split())

N = 1
K = 1

for i in range(k):
    N *= (n - i)
    K *= (k - i)

print((N // K) % 10007)