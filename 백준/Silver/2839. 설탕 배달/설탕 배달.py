N = int(input())
a, b = 0, N // 5
while b >= 0:
    if (N - b * 5) % 3 == 0: break
    else: b -= 1
print((N - b * 5) // 3 + b if (N - max(b, 0) * 5) % 3 == 0 else -1)