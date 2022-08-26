K = int(input())

ground = []
for i in range(6):
    a, b = map(int, input().split())
    ground.append([a, b])

ground = ground + ground

for i in range(len(ground)):
    if ground[i][0] == ground[i+2][0] and ground[i+1][0] == ground[i+3][0]:
        mini = ground[i+1][1] * ground[i+2][1]
        big = ground[i+4][1] * ground[i+5][1]
        break

print(f'{K * (big - mini)}')