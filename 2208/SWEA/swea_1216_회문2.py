'''
100x100 평면 글자판에서 가로, 세로를 모두 보아 가장 긴 회문의 길이를 구하는 문제이다.

각 칸의 들어가는 글자는 c언어 char type으로 주어지며 'A', 'B', 'C' 중 하나이다.

글자 판은 무조건 정사각형으로 주어진다.

ABA도 회문이며, ABBA도 회문이다. A또한 길이 1짜리 회문이다.

가로, 세로 각각에 대해서 직선으로만 판단한다.

    # 길이를 모르는 상황
    # 시작 글자와 끝 글자가 같다.
    # 찾은 길이보다 긴 것에서만 찾는다.
    # 인덱스 번호 + 길이 - 1 이 99(마지막 인덱스)을 초과하지 않을 때 까지
    # 리스트를 뒤집어서 비교 - 아님
'''
import sys

sys.stdin = open("swea_1216_회문2_v2.txt", "r")

test = 10

for t in range(1, test+1):
    trash = input()
    bingo = []
    for i in range(100):
        bingo.append(list(map(str, input().strip())))               # .strip()을 하면 문자 하나씩 받아짐

    result = 1 # 길이

    # # 리스트의 첫번째 행 첫번째 단어만 비교
    # for i in range(result +1, 101):              # i(길이) = result ~ 100
    #     if bingo[0][0] != bingo[0][0+i-1]:
    #         pass
    #     else:                                           # 같을 때
    #         for j in range(i//2):
    #             if bingo[0][0+j] == bingo[0][0+i-1-j]:
    #                 if j == range(i//2)[-1]:
    #                     result = i
    #             else:
    #                 break

    # # 리스트의 첫번째 행 k번째 단어 비교
    # for k in range(100):                                   # k = 0~99
    #     for i in range(result + 1, 101):  # i(길이) = result ~ 100
    #         if bingo[0][k] != bingo[0][k + i - 1]:
    #             pass
    #         else:  # 같을 때
    #             for j in range(i // 2):
    #                 if bingo[0][k + j] == bingo[0][k + i - 1 - j]:
    #                     if j == range(i // 2)[-1]:
    #                         result = i
    #                 else:
    #                     break

    # 리스트의 n번째 행 k번째 단어
    for n in range(100):
        for k in range(100):                                   # k = 0~99
            for i in range(result + 1, 101):  # i(길이) = result ~ 100
                if k + i - 1 >= 100:            # 오류 탈출용
                    break
                if bingo[n][k] != bingo[n][k + i - 1]:
                    pass
                else:  # 같을 때
                    for j in range(i // 2):
                        if bingo[n][k + j] == bingo[n][k + i - 1 - j]:
                            if j == range(i // 2)[-1]:
                                result = i
                        else:
                            break
            if k + result -1 >= 100:
                break

    bingo = list(zip(*bingo))       # 전치행렬

    for n in range(100):
        for k in range(100):                                   # k = 0~99
            for i in range(result + 1, 101):  # i(길이) = result ~ 100
                if k + i - 1 >= 100:        # 오류 탈출용
                    break
                if bingo[n][k] != bingo[n][k + i - 1]:
                    pass
                else:  # 같을 때
                    for j in range(i // 2):
                        if bingo[n][k + j] == bingo[n][k + i - 1 - j]:
                            if j == range(i // 2)[-1]:
                                result = i
                        else:
                            break
            if k + result -1 >= 100:
                break

    print(f'#{t} {result}')