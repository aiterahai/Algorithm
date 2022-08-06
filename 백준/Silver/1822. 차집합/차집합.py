from sys import stdin

N, M = map(int, stdin.readline().split())
result = sorted(list(set(list(map(int, stdin.readline().split()))) - set(list(map(int, stdin.readline().split())))))
if result: print(str(len(result)) + "\n" + " ".join(map(str, result)))
else: print(0)