n = int(input())
nums = tuple(map(int, input().split()))
clus = int(input())

result = 0
for num in nums:
    if num:
        result += num // clus
        if num % clus:
            result += 1

print(result * clus)