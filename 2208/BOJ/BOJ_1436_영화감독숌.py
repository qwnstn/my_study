'''
세트로 집합을 만들고
리스트로 변경해서 정렬 후
인덱스 출력
한자리수 10개 * 2    20 - 1(0일때)
두자리수 90개 * 3    270
세자리수 900개 * 4   3600
네자리수 1223개 * 5  (10000-3889) / 5  = 1223
6이 들어가면 중복
'''
'''
66600~66609까지 생략됨
'''
num666 = set()

for i in range(10000):
    num666.add(int(str(i) + '666'))
    num666.add(int('666' + str(i)))

    if i >= 10:
        num666.add(int(str(i // 10) + '666' + str(i)[-1::]))

    if i >= 100:
        num666.add(int(str(i // 100) + '666' + str(i)[-2::]))

    if i >= 1000:
        num666.add(int(str(i // 1000) + '666' + str(i)[-3::]))


num666 = list(num666)
num666.sort()

n = int(input())
for i in range(1, n+1):
    print(num666[i-1])