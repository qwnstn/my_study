from itertools import permutations
def make_p_list():
    global p_list
    p_list = [False, False, True] + [True, False] * (10000000 // 2)
    for i in range(3, 10000000, 2):
        if p_list[i]:
            for k in range(i, 10000000, i):
                p_list[k] = False
            p_list[i] = True

def solution(numbers):
    global p_list
    answer = 0
    make_p_list()
    num_list = set()
    for i in range(1, len(numbers)+1):
        for j in permutations(numbers, i):
            tmp = ''
            for k in j:
                tmp += k
            num_list.add(int(tmp))

    for num in num_list:
        if num:
            if p_list[num]:
                answer += 1
    return answer
from itertools import permutations
def make_p_list():
    global p_list
    p_list = [False, False, True] + [True, False] * (10000000 // 2)
    for i in range(3, 10000000, 2):
        if p_list[i]:
            for k in range(i, 10000000, i):
                p_list[k] = False
            p_list[i] = True

def solution(numbers):
    global p_list
    answer = 0
    make_p_list()
    num_list = set()
    for i in range(1, len(numbers)+1):
        for j in permutations(numbers, i):
            tmp = ''
            for k in j:
                tmp += k
            num_list.add(int(tmp))

    for num in num_list:
        if num:
            if p_list[num]:
                answer += 1
    return answer