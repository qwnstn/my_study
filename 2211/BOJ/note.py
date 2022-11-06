from collections import deque
a = [1,2,3,4,5]
a = deque(a)
a.appendleft(0)

print(list(a))