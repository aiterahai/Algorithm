from sys import stdin

board = []
def dfs(K):
    board.append(int(K))
    for i in range(int(K[-1])):
        dfs(K + str(i))

for i in range(10): dfs(str(i))
try: print(sorted(board)[int(stdin.readline())])
except: print(-1)