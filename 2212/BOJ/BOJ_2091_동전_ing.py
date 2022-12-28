def coin(X, A, B, C, D):
    result = [0, 0, 0, 0]
    result[0] = X % 5
    A -= result[0]
    if A < 0:
        print(0, 0, 0, 0)
        return
    result[0] +=


X, A, B, C, D = map(int, input().split())
# A, 5 B, 10 C, 25 D

coin(X, A, B, C, D)





