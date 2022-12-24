elixer = {239: 1, 229: 2, 219: 4, 209: 8}
answer = {1: 4, 2: 3, 4: 2, 8: 1}

n = int(input())
level = 0

for k, v in elixer.items():
    if n > k:
        continue
    tmp = n + v
    if tmp > k:
        tmp = k + 1

    if level < tmp:
        level = tmp
        result = answer[v]

print(result)