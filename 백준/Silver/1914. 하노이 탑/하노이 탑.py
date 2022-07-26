def hanoi(start, prev, end, N):
    if N == 1: print(start, end); return
    hanoi(start, end, prev, N - 1)
    print(start, end)
    hanoi(prev, start, end, N - 1)

K = int(input())
print(2 ** K - 1)
if K <= 20: hanoi(1, 2, 3, K)