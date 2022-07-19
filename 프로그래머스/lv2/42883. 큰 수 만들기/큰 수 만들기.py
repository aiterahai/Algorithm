def solution(number, k):
    stack = []
    for i in number:
        stack.append(i)
        while len(stack) >= 2 and k and int(stack[-2]) < int(stack[-1]):
            temp = stack.pop()
            stack.pop()
            stack.append(temp)
            k -= 1
    return "".join(map(str, stack[:len(stack)-k]))