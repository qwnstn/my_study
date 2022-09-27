import heapq

h =[]
heapq.heapify(h)
heapq.heappush(h, 1)
heapq.heappush(h, 3)
heapq.heappush(h, 2)
print(heapq.heappop(h))