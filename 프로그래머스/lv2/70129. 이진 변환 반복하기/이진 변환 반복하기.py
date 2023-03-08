def solution(s):
    t, d = 0, 0
    while s != "1":
        d += s.count("0")
        s = bin(len(s.replace("0", "")))[2:]
        t += 1

    return [t, d]