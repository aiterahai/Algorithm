from sys import stdin

a, b = map(int, stdin.readline().split())
result = str(a // b) + "."
a %= b
for _ in range(1000):
    a *= 10
    result += str(a // b)
    a %= b
print(result)