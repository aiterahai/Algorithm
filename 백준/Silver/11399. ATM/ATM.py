n = int(input())
arr = sorted(map(int, input().split()), reverse=True)
time = 0
for i in range(n):
    time += arr[i]*(i+1)
print(time)