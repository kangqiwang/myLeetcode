import heapq
# heapData = [10, 50, 60, 20, 70]
# heapq.heapify(heapData)
# print("Heap:")
# print(heapData)
# heapq.heappush(heapData, 40)
# print(heapData)
# heapq.heappush(heapData, 30)
# print(heapData)

# heapq.heappop(heapData)
lists= [[1,4,5],[1,3,4],[2,6]]
h=[(1, 0), (1, 1), (2, 2)]
while h:
    print(h)
    val,i=heapq.heappop(h)
    # print("val = ",val)
    # print("i=",i)
    print(lists[i])
    if lists[i]:
        heapq.heappush(h,(lists[i],i))