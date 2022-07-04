N = int(input())
print(sum([(N//i)*i for i in range(1, N+1)]))