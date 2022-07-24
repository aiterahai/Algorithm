def hanoi(start, temp, end, N):
    if N == 1: print(start, end); return
    hanoi(start, end, temp, N - 1)
    print(start, end)
    hanoi(temp, start, end, N - 1)
N = int(input())
print(2 ** N - 1)
hanoi(1, 2, 3, N)