from sys import stdin

def binary_search(value, start, end):
    mid = (start + end) // 2
    if start > end: return mid
    if value <= B[mid]: return binary_search(value, start, mid - 1)
    if value > B[mid]: return binary_search(value, mid + 1, end)

for _ in range(int(stdin.readline())):
    N, M = map(int, stdin.readline().split())
    A, B = list(map(int, stdin.readline().split())), sorted(list(map(int, stdin.readline().split())))
    count = sum(binary_search(i, 0, M - 1) for i in A) + len(A)
    print(count)