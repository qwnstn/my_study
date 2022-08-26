N = int(input())

num = list(map(int, input().split()))

result_up = 1
cnt = 1
for i in range(N-1):
    if cnt == 1 and i + result_up > N:
        break

    if num[i] <= num[i + 1]:           # 증가할 때
        cnt += 1
    else:
        if result_up < cnt:
            result_up = cnt
        cnt = 1
if result_up < cnt:
    result_up = cnt


result_down = 1
cnt = 1
for i in range(N-1):
    if cnt == 1 and i + result_down > N:
        break

    if num[i] >= num[i + 1]:           # 감소할 때
        cnt += 1
    else:
        if result_down < cnt:
            result_down = cnt
        cnt = 1
if result_down < cnt:
    result_down = cnt

print(max(result_up, result_down))