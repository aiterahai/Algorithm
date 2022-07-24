def count(a, b):
    count = 0
    while a >= b:
        a = a // b
        count += a
    return count
N, M = map(int, input().split())
print(min(count(N, 2) - count(M, 2) - count(N - M, 2), count(N, 5) - count(M, 5) - count(N - M, 5)))