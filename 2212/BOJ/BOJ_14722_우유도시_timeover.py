import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def dfs(x, y, milk, d, count):  # 현재 위치(x, y), 우유 체크, 이동할 곳, 결과값
    global result
    if x == n-1 and y == n-1:
        if ground[x][y] == milk:
            new_count = count + 1
        else:
            new_count = count

        if result < new_count:
            result = new_count
        return

    elif 0 <= x < n and 0 <= y < n:
        if ground[x][y] == milk:
            new_count = count + 1
            new_milk = (milk + 1) % 3
        else:
            new_count = count
            new_milk = milk

        if d == '10':
            dfs(x + 1, y, new_milk, '10', new_count)
            dfs(x + 1, y, new_milk, '01', new_count)
        else:
            dfs(x, y + 1, new_milk, '10', new_count)
            dfs(x, y + 1, new_milk, '01', new_count)

n = int(input())
ground = [list(map(int, input().split())) for _ in range(n)]
result = 0

dfs(0, 0, 0, '10', 0)
dfs(0, 0, 0, '01', 0)

print(result)