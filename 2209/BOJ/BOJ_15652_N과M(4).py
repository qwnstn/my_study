'''
자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

1부터 N까지 자연수 중에서 M개를 고른 수열
같은 수를 여러 번 골라도 된다.
고른 수열은 비내림차순이어야 한다.
길이가 K인 수열 A가 A1 ≤ A2 ≤ ... ≤ AK-1 ≤ AK를 만족하면, 비내림차순이라고 한다.
'''
def card(n, m, s): # n = 최대 카드 숫자, m = 길이, s = 시작 카드 숫자
    global ck

    if len(ck) != m:
        for i in range(s, n+1):
            ck += str(i)
            card(n, m, i)
            ck = ck[0:-1]

    else:
        result.append(ck)

n, m = map(int, input().split())
result = []
ck = ''
card(n, m, 1)
for _ in result:
    print(*_)