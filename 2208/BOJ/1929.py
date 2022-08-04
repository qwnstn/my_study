m, n = map(int, input().split())

p_list = [False, False] + [True] * (n-1)

for i in range(n+1):
    if p_list[i]:
        for j in range(2, n//i +1):
            p_list[i*j] = False

for num, v in enumerate(p_list):
    if v:
        if num >= m:
            print(num)