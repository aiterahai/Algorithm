def solution(arr):
    result = [arr[0]]
    for i in arr[1:]:
        result.append(i)
        if result[-1] == result[-2]: result.pop()
    return result