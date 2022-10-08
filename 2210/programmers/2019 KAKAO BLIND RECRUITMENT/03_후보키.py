'''
관계 데이터베이스에서 릴레이션(Relation)의 튜플(Tuple)을 유일하게 식별할 수 있는
속성(Attribute) 또는 속성의 집합 중, 다음 두 성질을 만족하는 것을 후보 키(Candidate Key)라고 한다.

유일성(uniqueness) : 릴레이션에 있는 모든 튜플에 대해 유일하게 식별되어야 한다.
최소성(minimality) : 유일성을 가진 키를 구성하는 속성(Attribute) 중 하나라도 제외하는 경우
                    유일성이 깨지는 것을 의미한다.
                    즉, 릴레이션의 모든 튜플을 유일하게 식별하는 데 꼭 필요한 속성들로만 구성되어야 한다.
'''
'''
학번  이름      전공      학년
100   r         music    2
200   a         math     2
300   t         computer 3
400   c         computer 1
500   m         music    3
600   a         music    2

위의 예를 설명하면, 학생의 인적사항 릴레이션에서 모든 학생은 각자 유일한 "학번"을 가지고 있다.
따라서 "학번"은 릴레이션의 후보 키가 될 수 있다.

그다음 "이름"에 대해서는 같은 이름("apeach")을 사용하는 학생이 있기 때문에,"이름"은 후보 키가 될 수 없다.
그러나, 만약 ["이름", "전공"]을 함께 사용한다면 릴레이션의 모든 튜플을 유일하게 식별 가능하므로
후보 키가 될 수 있게 된다.

물론 ["이름", "전공", "학년"]을 함께 사용해도 릴레이션의 모든 튜플을 유일하게 식별할 수 있지만,
최소성을 만족하지 못하기 때문에 후보 키가 될 수 없다.

따라서, 위의 학생 인적사항의 후보키는 "학번", ["이름", "전공"] 두 개가 된다.

릴레이션을 나타내는 문자열 배열 relation이 매개변수로 주어질 때,
이 릴레이션에서 후보 키의 개수를 return 하도록 solution 함수를 완성하라.
'''
'''
relation은 2차원 문자열 배열이다.
relation의 컬럼(column)의 길이는 1 이상 8 이하이며, 각각의 컬럼은 릴레이션의 속성을 나타낸다.
relation의 로우(row)의 길이는 1 이상 20 이하이며, 각각의 로우는 릴레이션의 튜플을 나타낸다.
relation의 모든 문자열의 길이는 1 이상 8 이하이며, 알파벳 소문자와 숫자로만 이루어져 있다.
relation의 모든 튜플은 유일하게 식별 가능하다.(즉, 중복되는 튜플은 없다.)
'''
from itertools import combinations

def solution(relation):
    answer = 0
    N = len(relation)       # 로우 길이(행 개수), 최대 8
    n = len(relation[0])    # 컬럼 개수(열 개수), 최대 20

    skip = []               # 무시 가능한 조합
    total = 2**n - 1

    ck = 0
    while total:
        ck += 1
        # 조합 구하기
        combi = list(combinations(range(n), ck))
        tmp_set = [set() for _ in range(len(combi))]

        for r in relation:
            for i, v in enumerate(r):
                tmp_set[i].add(v)

        for i, v in enumerate(tmp_set):
            if len(v) == N:
                answer += 1
                skip.append(i)
                total -= 2**i

    next


    return answer

print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))
'''
2
'''