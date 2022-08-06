from sys import stdin

N, K = map(int, stdin.readline().split())
print(sorted(list(map(int, stdin.readline().split())))[-K])