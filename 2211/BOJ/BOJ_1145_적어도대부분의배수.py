num = list(map(int, input().split()))
num.sort()

k = num[2] - 1
while True:
    k += 1
    ck = 0

    for n in num:
        if k % n == 0:
            ck += 1

    if ck > 2:
        print(k)
        break