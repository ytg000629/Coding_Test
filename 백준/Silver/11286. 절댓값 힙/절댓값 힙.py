import heapq
import sys
input = sys.stdin.readline

n = int(input())
heap = []

for i in range(n):
    
    value = int(input())
    
    if value == 0:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
    else:
        heapq.heappush(heap, (abs(value), value))