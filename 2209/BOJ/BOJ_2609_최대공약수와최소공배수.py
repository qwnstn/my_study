a, b = map(int, input().split())

result_1 = 1            # 최대공약수
result_2 = 0    # 최소공배수

# 최대공약수
if max(a, b) % min(a, b) == 0:
    result_1 = min(a, b)
    result_2 = max(a, b)
else:
    ck = min(a, b) // 2
    while ck:
        if a % ck == 0 and b % ck == 0:
            result_1 = ck
            break
        ck -= 1

    # 최소공배수
    result_2 = max(a, b) * min(a, b) // result_1

print(result_1)
print(result_2)