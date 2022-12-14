'''
현주는 1번부터 N번까지 N개의 상자를 가지고 있다. 각 상자에는 숫자를 새길 수 있는데 처음에는 모두 0으로 적혀있다.

숫자가 너무 단조로웠던 현주는 다음 Q회 동안 일정 범위의 연속한 상자를 동일한 숫자로 변경하려고 한다.
변경하는 방법은 다음과 같다.

   ·  i (1 ≤ i ≤ Q)번째 작업에 대해 L번 상자부터 R번 상자까지의 값을 i로 변경

현주가 Q회 동안 위의 작업을 순서대로 한 다음 N개의 상자에 적혀있는 값들을 순서대로 출력하는 프로그램을 작성하라.
'''

t = int(input())

for x in range(1, t + 1):
    n, q = map(int, input().split())
    n_box = [0] * n
    for i in range(1, q+1):
        l, r = map(int, input().split())

        for k, v in enumerate(n_box):
            if l-1 <= k <= r-1:
                n_box[k] = i

    print(f'#{x}', *n_box)