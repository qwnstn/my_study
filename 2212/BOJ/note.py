asd = {1:{1,2}, 2:{4,5}, 3:{6,7}}

for k, value in asd.items():
    tmp = set()
    for v in value:
        tmp.add(v * 10)
    asd[k] = asd[k] | tmp
print(asd)