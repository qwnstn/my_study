'''
둘째 줄부터 N개의 줄에 동전의 가치 Ai가 오름차순으로 주어진다. (1 ≤ Ai ≤ 1,000,000, A1 = 1, i ≥ 2인 경우에 Ai는 Ai-1의 배수)
'''

n, k = map(int, input().split())
coin = [int(input()) for i in range(n)]

result = 0
for i in range(-1, -n-1, -1):
    result += k // coin[i]
    k -= (k // coin[i]) * coin[i]

print(result)