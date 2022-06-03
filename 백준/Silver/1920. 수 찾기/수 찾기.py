n = int(input())
arr = sorted(list(map(int, input().split())))
m = int(input())
find = list(map(int, input().split()))

def binary_search(arr, value, left, right):
    middle = (left + right)//2
    if(left > right):
        return 0;
    elif(value == arr[middle]):
        return 1;
    elif(value < arr[middle]):
        return binary_search(arr, value, left, middle-1)
    else:
        return binary_search(arr, value, middle+1, right)

for i in find:
    print(binary_search(arr, i, 0, len(arr)-1))