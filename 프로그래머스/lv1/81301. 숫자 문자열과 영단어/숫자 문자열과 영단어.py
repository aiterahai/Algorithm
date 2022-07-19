def solution(s):
    for i, j in enumerate(["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]): s = s.replace(j, str(i))
    return int(s)