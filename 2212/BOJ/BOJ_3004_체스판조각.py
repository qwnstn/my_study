n = int(input())

row = 1 + n // 2
column = 1 + n // 2

if n % 2:
    row += 1

print(row * column)