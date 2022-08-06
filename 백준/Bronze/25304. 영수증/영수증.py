from sys import stdin

X = int(stdin.readline())
N = int(stdin.readline())
for _ in range(N):
    A, B = map(int, stdin.readline().split())
    X -= A * B
print('No' if X else 'Yes')