L = int(input())
nums = sorted(list(map(int, input().split())))
n = int(input())

start, end, done = 1, 1000, 0
for num in nums:
    if n > num:
        start = num + 1
    elif n < num:
        end = num - 1
        break
    elif n == num:
        done = 1
        break

if done:
    print(0)
else:
    if start == end:
        print(0)
    elif start == n or end == n:
        print(end - start)
    else:
        print((n-start)*(end-n) + (end-start))