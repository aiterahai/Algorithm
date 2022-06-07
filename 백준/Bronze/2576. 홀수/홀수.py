from sys import stdin
arr = [int(stdin.readline()) for i in range(7)]
odds = []
for i in arr:
    if i % 2 == 1: odds.append(i)
if(len(odds) == 0): print(-1)
else:
    print(sum(odds))
    print(min(odds))