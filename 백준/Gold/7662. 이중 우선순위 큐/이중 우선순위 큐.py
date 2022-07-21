from sys import stdin
import heapq

for _ in range(int(stdin.readline())):
    maxheap, minheap = [], []
    visit = [0 for i in range(1000001)]
    for i in range(int(stdin.readline())):
        command = stdin.readline().split()
        if command[0] == "I":
            heapq.heappush(maxheap, (-int(command[1]), i))
            heapq.heappush(minheap, (int(command[1]), i))
            visit[i] = 1
        elif command[1] == "1":
            while maxheap and not visit[maxheap[0][1]]: heapq.heappop(maxheap)
            if maxheap:
                visit[maxheap[0][1]] = 0
                heapq.heappop(maxheap)
        else:
            while minheap and not visit[minheap[0][1]]: heapq.heappop(minheap)
            if minheap:
                visit[minheap[0][1]] = 0
                heapq.heappop(minheap)
    while maxheap and not visit[maxheap[0][1]]: heapq.heappop(maxheap)
    while minheap and not visit[minheap[0][1]]: heapq.heappop(minheap)
    if minheap and maxheap: print(-maxheap[0][0], minheap[0][0])
    else: print("EMPTY")