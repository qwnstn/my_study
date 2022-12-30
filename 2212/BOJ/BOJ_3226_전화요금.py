N = int(input())

result = 0
for _ in range(N):
    HHMM, DD = map(str, input().split())

    HH = int(HHMM[:2])
    MM = int(HHMM[3:])
    DD = int(DD)

    while DD:
        DD -= 1
        if 7 <= HH <= 18:
            result += 10
        else:
            result += 5

        MM += 1
        if MM == 60:
            MM = 0
            HH += 1

print(result)