from itertools import permutations

def solution(info, query):
    answer = []
    language = {'cpp', 'java', 'python'}
    fb = {'backend', 'frontend'}
    js = {'junior', 'senior'}
    soul = {'chicken', 'pizza'}

    d = dict()
    for l in language:
        for f in fb:
            for j in js:
                for s in soul:
                    tmp = l[0] + f[0] + j[0] + s[0]
                    d[tmp] = []

    for i in info:
        l,f,j,s,sc = i.split()
        tmp = l[0] + f[0] + j[0] + s[0]
        d[tmp].append(sc)
    print(d)

    for q in query:
        l,f,j,s,sc = q.split(' and ')
        tmp = l[0] + f[0] + j[0] + s[0]
        # '-'문자열이 포함되면 어떻게 해야하나?
        for k, v in d.items():







    return answer

solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"])