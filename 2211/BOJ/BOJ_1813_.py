n = int(input())
nums = list(map(int, input().split()))

num_d = {i:0 for i in range(50, -1, -1)}

for num in nums:
    num_d[num] += 1

for k, v in num_d.items():
    if k == v:
        print(k)
        break
    elif k == 0:
        print(-1)