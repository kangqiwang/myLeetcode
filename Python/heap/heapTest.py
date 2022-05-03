import heapq
heapData = [10, 50, 60, 20, 70]
heapq.heapify(heapData)
print("Heap:")
print(heapData)
heapq.heappush(heapData, 40)
print(heapData)
heapq.heappush(heapData, 30)
print(heapData)

heapq.heappop(heapData)
print(heapData)