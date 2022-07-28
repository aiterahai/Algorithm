from sys import stdin

for _ in range(int(stdin.readline())):
    stdin.readline()
    board = [int(stdin.readline()) for i in range(int(stdin.readline()))]
    print("YES" if sum(board) % len(board) == 0 else "NO")