N=int(input())
distance=list(map(int,input().split()))
values=list(map(int,input().split()))

result=0
temp=int(1e9)
for i in range(N-1):
  temp=min(temp,values[i])
  result+=temp*distance[i]
print(result)