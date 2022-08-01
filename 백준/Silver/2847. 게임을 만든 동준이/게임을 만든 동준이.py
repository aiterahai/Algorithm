from sys import stdin

N = int(stdin.readline())
board = [int(stdin.readline()) for _ in range(N)][::-1]
score = [board[0]]
for i in range(1, N): score.append(min(score[i-1] - 1, board[i]))
print(sum([board[i] - score[i] for i in range(N)]))