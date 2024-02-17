import heapq

h = [100, 20, 50, 40, 60, 30, 70]
heap=[]
for i in h:
    heapq.heappush(heap, i)

heapq.heappush(heap, 2)
heapq.heappush(heap, 10)
heapq.heappush(heap, 98)
heapq.heappush(heap, 97)
heapq.heappush(heap, 96)
heapq.heappush(heap, 54)
print(heap)

heapq.heappop(heap)
print(heap)

heapq.heapify(h)

print(heapq.nlargest(2, heap))
print(h)

while h:
    smallest = heapq.heappop(h)
    print(smallest)
