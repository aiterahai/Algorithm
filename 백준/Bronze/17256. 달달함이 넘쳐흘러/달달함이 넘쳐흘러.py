a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(*[b[0]-a[2], b[1]//a[1], b[2]-a[0]])