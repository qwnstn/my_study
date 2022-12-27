def solution(s):
    zxc = set(s.strip("{}").split("},{"))
    print('zxc', zxc)
    sort = dict()
    for i in zxc:
        sort[len(i)] = set(i)
    print('sort', sort)

    key = 1
    answer = []
    tmp_answer = {','}
    answer += list(sort[key] - tmp_answer)
    tmp_answer = tmp_answer | (sort[key] - tmp_answer)
    while True:
        key += 2
        try:
            answer += list(sort[key] - tmp_answer)
            tmp_answer = tmp_answer | (sort[key] - tmp_answer)
        except:
            break
    return answer

asd = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
# print(asd)
solution(asd)