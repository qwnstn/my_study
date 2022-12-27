def solution(begin, end):
    answer = [1 for _ in range(begin, end+1)]
    for i in range(begin, end+1):
        if i % 2 == 0:
                answer[i - begin] = i//2
        else:
            for j in range(3, int(i**0.5)+1, 2):
                if i % j == 0:
                    answer[i - begin] = i//j
                    break

    if begin == 1:
        answer[0] = 0
    print(answer)
    return answer

solution(1, 10)