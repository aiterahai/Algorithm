from sys import stdin

P, K = map(int, stdin.readline().split())
for i in range(2, K):
    if P % i == 0: print(f"BAD {i}"); exit(0)
print("GOOD")