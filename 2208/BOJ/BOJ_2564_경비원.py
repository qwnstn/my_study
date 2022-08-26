'''
----------  ------  ------------  -------
    남       서    0     북          동
'''

rk, tp = map(int, input().split())
n = int(input())
store = []
for i in range(n):
    a, b = map(int, input().split())
    store.append([a, b])
dong = list(map(int, input().split()))
result = []



if dong[0] == 1:  # 북쪽(상단) - 기준
    ck = dong[1]
elif dong[0] == 2:  # 남쪽(하단)
    ck = -tp - dong[1]  # 좌측 훑기
elif dong[0] == 3:  # 서쪽(좌측)
    ck = -dong[1]
else:  # 동쪽(우측)
    ck = rk + dong[1]


for i in store:
    N = []
    S = []
    W = []
    E = []
    if i[0] == 1:       # 북쪽(상단) - 기준
        N.append(i[1])
        N.append(N[0] + (rk + tp) * 2)
        N.append(N[0] - (rk + tp) * 2)
    elif i[0] == 2:     # 남쪽(하단)
        S.append(-tp - i[1])         # 좌측 훑기
        S.append(S[0] + (rk + tp) * 2)
        S.append(S[0] - (rk + tp) * 2)
    elif i[0] == 3:     # 서쪽(좌측)
        W.append(-i[1])
        W.append(W[0] + (rk + tp) * 2)
        W.append(W[0] - (rk + tp) * 2)
    else:               # 동쪽(우측)
        E.append(rk + i[1])
        E.append(E[0] + (rk + tp) * 2)
        E.append(E[0] - (rk + tp) * 2)

    for d in [N, S, E, W]:
        if d:
            t = rk + tp
            for k in d:
                if t > abs(ck - k):
                    t = abs(ck - k)
            result.append(t)

print(sum(result))