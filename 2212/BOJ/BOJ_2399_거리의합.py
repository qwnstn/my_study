n = int(input())

nums = list(map(int, input().split()))

nums.sort(reverse=True)

result = 0
for i in range(n):
    result += nums[i] * (n-2*i-1)

print(result * 2)