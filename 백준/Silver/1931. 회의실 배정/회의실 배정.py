from sys import stdin

board = sorted([list(map(int, stdin.readline().split())) for i in range(int(stdin.readline()))], key = lambda x : (x[0], x[1]))
result, board = [board[0]], board[1:]
for i in board:
    if i[1] < result[-1][1]: result[-1] = i
    elif i[0] >= result[-1][1]: result.append(i)
print(len(result))