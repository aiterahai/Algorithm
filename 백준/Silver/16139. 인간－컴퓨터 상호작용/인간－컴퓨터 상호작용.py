from sys import stdin, stdout

string = stdin.readline().strip()
board = [[0 for _ in range(26)] for _ in range(len(string))]
board[0][ord(string[0]) - 97] = 1
for i in range(1, len(string)):
    board[i][ord(string[i]) - 97] = 1
    for j in range(26): board[i][j] += board[i - 1][j]
for _ in range(int(stdin.readline())):
    A, B, C = stdin.readline().split()
    if int(B) == 0: stdout.write(f"{board[int(C)][ord(A) - 97]}\n")
    else: stdout.write(f"{board[int(C)][ord(A) - 97] - board[int(B) - 1][ord(A) - 97]}\n")