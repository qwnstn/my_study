def solution(relation):
    answer = []
    N = len(relation)       # 로우 길이(행 개수), 최대 8
    M = len(relation[0])    # 컬럼 개수(열 개수), 최대 20
    for i in range(1 << M):
        cnt = []
        for j in range(M):
            if i & (1 << j):
                cnt.append(j)       # 인덱스 부분 집합
        A = set(tuple(relation[k][l] for l in cnt) for k in range(N))   # 부분 집합

        if len(A) == N:
            answer.append(i)

    cnt = 0
    for i in answer:
        for j in answer:
            if i != j and i | j == i:
                cnt += 1
                break
    return len(answer) - cnt

print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))