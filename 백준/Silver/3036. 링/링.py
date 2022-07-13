from math import gcd

N = int(input())
board = list(map(int, input().split()))
for i in range(1, len(board)):
    print(f"{board[0] // gcd(board[0], board[i])}/{board[i] // gcd(board[0], board[i])}")