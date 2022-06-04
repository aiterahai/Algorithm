from collections import deque
n, k = map(int, input().split())
peoples = deque([i for i in range(1, n+1)])
results = []
counts = 1
while(len(results) != n):
    if(counts % k == 0):
        results.append(peoples.popleft())
        counts += 1
    else:
        peoples.append(peoples.popleft())
        counts += 1
print(str(results).replace('[', '<').replace(']', '>'))