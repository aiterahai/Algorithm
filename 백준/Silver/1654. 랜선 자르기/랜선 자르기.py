from sys import stdin
k, n = map(int, stdin.readline().split())
cable = [int(stdin.readline()) for i in range(k)]
def binary_search(start, end):
    middle = (start + end) // 2
    temp = sum([cable[i] // middle for i in range(k)])
    if(start > end):
        return middle
    if(temp == n and start > end):
        return middle
    if(temp < n):
        return binary_search(start, middle - 1)
    return binary_search(middle + 1, end)

print(binary_search(1, max(cable)))