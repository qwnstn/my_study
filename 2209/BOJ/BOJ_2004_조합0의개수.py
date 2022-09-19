'''
5의 개수
2의 개수
'''

n, k = map(int, input().split())

# n에서 5의 개수
n_5 = 0
ck = 1
while n // 5 ** ck != 0:
    n_5 += n // 5**ck
    ck += 1

ck = 1
while (n - k) // 5 ** ck != 0:
    n_5 -= (n - k) // 5 ** ck
    ck += 1


# n에서 2의 개수
n_2 = 0
ck = 1
while n // 2 ** ck != 0:
    n_2 += n // 2 ** ck
    ck += 1

ck = 1
while (n - k) // 2 ** ck != 0:
    n_2 -= (n - k) // 2 ** ck
    ck += 1

# k에서 5의 개수
k_5 = 0
ck = 1
while k // 5 ** ck != 0:
    k_5 += k // 5**ck
    ck += 1

# k에서 2의 개수
k_2 = 0
ck = 1
while k // 2 ** ck != 0:
    k_2 += k // 2**ck
    ck += 1

print(min(n_5 - k_5, n_2 - k_2))