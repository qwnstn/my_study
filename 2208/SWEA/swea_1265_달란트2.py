import sys
sys.stdin = open('swea_1265_달란트2.txt', 'r')

test = int(input())

for t in range(1, test + 1):
    a, b = map(int, input().split())
    x = a // b
    print(f'#{t} {x**(b - a%b) * (x+1)**(a%b)}')