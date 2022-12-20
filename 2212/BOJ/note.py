from collections import deque
asd = [3]
asd = deque([[[3]]])


while asd:
    asd.popleft()
    print('진행중')

print('끝', asd)