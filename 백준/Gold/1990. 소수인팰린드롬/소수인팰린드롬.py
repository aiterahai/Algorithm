from sys import stdin

isprime = [True] * 10000001
isprime[0], isprime[1] = False, False
for i in range(2, int(10000001 ** 0.5) + 1):
    if not isprime[i]: continue
    for j in range(i ** 2, 10000001, i):
        isprime[j] = False
prime = [i for i in range(10000001) if isprime[i]]
palinPrime = [i for i in prime if str(i) == str(i)[::-1]]
A, B = map(int, stdin.readline().split())
for i in palinPrime:
    if A <= i <= B: print(i)
print(-1)