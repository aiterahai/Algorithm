from sys import stdin
prime = [0, 0] + [1 for i in range(9999)]
for i in range(2, int(10001 ** 0.5) + 1):
    if not prime[i]: continue
    for j in range(i * 2, 10001, i): prime[j] = 0
for _ in range(int(stdin.readline())):
    N = int(stdin.readline())
    for i in range(N // 2, 0, -1):
        if prime[N - i] and prime[i]:
            print(i, N - i); break