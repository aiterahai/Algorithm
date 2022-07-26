from sys import stdin

N, K = map(int, stdin.readline().split())
board = stdin.readline().strip()
temp = []
for i in board:
    temp.append(i)
    while len(temp) >= 2 and K > 0 and temp[-2] < temp[-1]:
        K -= 1
        t = temp.pop()
        temp.pop()
        temp.append(t)
for i in range(K): temp.pop()
print("".join(map(str, temp)))