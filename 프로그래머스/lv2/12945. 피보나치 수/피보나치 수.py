def solution(n):
    arr = [0, 1]
    for i in range(n): arr[i%2] = sum(arr) % 1234567
    return arr[n%2]