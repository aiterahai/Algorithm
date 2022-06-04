from collections import deque
from sys import stdin

n, k = map(int, stdin.readline().split())

arr = deque([i for i in range(1, n+1)])
result = []

while len(arr) != 0:
  for _ in range(k-1):
    arr.append(arr.popleft())

  result.append(arr.popleft())

print(str(result).replace('[', '<').replace(']', '>'))