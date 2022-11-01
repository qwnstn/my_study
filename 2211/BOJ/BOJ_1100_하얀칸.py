chess = []
for i in range(8):
    chess.append(input())

result = 0
for i in range(8):
    for j in range(8):
        if chess[i][j] == 'F':
            if not (i + j) % 2:
                result += 1

print(result)