n, k = map(int, input().split())

N = 1
K = 1

if k <= n//2:
    for i in range(k):
        N *= (n - i)
        K *= (k - i)
else:
    k = n - k
    for i in range(k):
        N *= (n - i)
        K *= (k - i)

print((N // K) % 10007)