import heapq
from sys import stdin

command = [int(stdin.readline()) for i in range(int(stdin.readline()))][::-1]
heap = []
while command:
    i = command.pop()
    if i == 0:
        if len(heap) == 0:
            print(0)
        else: print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap, (-i, i))