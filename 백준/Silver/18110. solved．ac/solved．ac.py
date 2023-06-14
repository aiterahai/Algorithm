from sys import stdin


def my_round(num):
    return int(num) + (1 if num - int(num) >= 0.5 else 0)


N = int(stdin.readline())
if not N:
    print(0)
    exit(0)
board = sorted([int(stdin.readline()) for _ in range(N)])
board = board[my_round(len(board) * 0.15) : N - my_round(len(board) * 0.15)]
print(my_round(sum(board) / len(board)))