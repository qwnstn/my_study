import sys
input = sys.stdin.readline

n = int(input())
num_list = list(map(int, input().split()))

new = sorted(list(set(num_list)))               # 중복 제거 후 정렬

num_dict = {v: i for i, v in enumerate(new)}    # {숫자: 본인보다 작은 수의 개수(= 인덱스 번호)}

result = [num_dict[num_list[i]] for i in range(len(num_list))]  # 딕셔너리에서 값 가져오기

print(' '.join(map(str, result)))