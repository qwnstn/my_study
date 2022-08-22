#  솔루션 코드를 작성합니다.
T = int(input())

for test_case in range(1, T + 1):
    d, M, T, Y = map(int, input().split())
    M = min(M, T, Y)
    T = min(M * 3, T, Y)
    Y = min(Y, 4 * T, 12 * M)
    DP = [min(i * d, M) for i in map(int, input().split())]  # 1달 이용권 최저값

    Min = Y  # 최솟값 기준
    stack = {(0, 0)}  # 길이,가격
    while stack:
        L, P = stack.pop()

        if L >= 12:
            Min = min(Min, P)
        elif L < 12:
            stack.add((L + 1, P + DP[L]))
            stack.add((L + 3, P + T))
            stack.add((L + 12, P + Y))
    print(f'#{test_case}', Min)

    상황 : 고점은 일정하게 정해짐
    p   평균이 a이상인 집단이 두 개라면
    q   두 집단의 절반조합 어느거나 평균은 a이상이다.

    110 90 110 110 110 90