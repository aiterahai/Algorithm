arr = []
for i in range(int(input())):
    temp = int(input())
    if(temp == 0):
        arr.pop()
    else:
        arr.append(temp)
print(sum(arr))