import heapq
a = dict()

h = [4]
heapq.heapify(h)
print(h)
for i in range(2):
    a[i] = h[:]
print(a)

print(a)
heapq.heappush(a[1], 1)
heapq.heappush(a[1], 3)
heapq.heappush(a[1], 2)
print(type(h))
print(a)