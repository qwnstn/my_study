'''
딕셔너리로 받는다. {나이 : [이름 리스트]}

정렬이 필요하므로 리스트로 변경

정렬 후 출력
'''
import sys
n = int(sys.stdin.readline())

namedict = dict()
for i in range(n):
    a, b = map(str, sys.stdin.readline().split())
    a = int(a)                                      # 나중에 정렬해야하므로 미리 숫자로 변경
    if namedict.get(a) == None:                     # 받은 key(나이)가 새로운 것일 경우
        namedict[a] = [b]                           # (중요) [이름]으로 바로 받음.
    else:
        namedict[a].append(b)                       # key가 기존에 있는 경우 value 리스트에 추가
                                                    # 위에서 리스트로 받았기 때문에 바로 append가 가능

namelist = []                                       # 딕셔너리를 리스트로 변경
for k, v in namedict.items():
    namelist.append([k] + v)                        # [[21, 이름1, 이름2], [20, 이름3]]

namelist.sort(key=lambda x: x[0])                   # 나이 기준으로 정렬

for i in namelist:
    for k in range(1, len(i)):                      # 나이는 인덱스 0에 고정
        print(i[0], i[k])                           # 순서대로 출력