from sys import stdin

arr = [int(stdin.readline()) for i in range(5)]
print(int(sum(arr)/5))
print(sorted(arr)[2])