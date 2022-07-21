N = int(input())

def palindrome(number): return 1 if str(number) == str(number)[::-1] else 0

visit = [0, 0] + [1 for i in range(1100000)]
idx = 0
for i in range(2, int(1100000 ** 0.5) + 1):
    if not visit[i]: continue
    for j in range(i * 2, 1100000, i): visit[j] = 0
prime = [i for i in range(1100000) if visit[i] and palindrome(i)]
while prime[idx] < N: idx += 1
print(prime[idx])