from sys import stdin

N = int(stdin.readline())
result = 1
for i in range(1, N + 1):
    result = int(str(result * i).rstrip("0")) % 10000000
print(str(result).rstrip("0")[-1])