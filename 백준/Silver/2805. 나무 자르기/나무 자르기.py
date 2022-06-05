n, m = map(int, input().split())
trees = list(map(int, input().split()))

def binary_search(start, end, value):
    middle = (start+end) // 2
    temp = 0
    for i in trees:
        if(i - middle > 0): temp += i - middle
    if(start > end): return middle
    elif(temp == value):
        return middle
    elif(temp > value):
        return binary_search(middle+1, end, value)
    elif(temp < value):
        return binary_search(start, middle-1, value)
print(binary_search(0, max(trees), m))