def computeLPS(pat, lps):
    length = 0
    i = 1
    while i < len(pat):
        if pat[i] == pat[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length: length = lps[length-1]
            else:
                lps[i] = 0
                i += 1

def KMP(pat, txt):
    global result, F
    M, N, lps, i, j = len(pat), len(txt), [0] * len(pat), 0, 0
    computeLPS(pat, lps)
    while i < N:
        if pat[j] == txt[i]: i, j = i + 1, j + 1
        elif pat[j] != txt[i]:
            if j: j = lps[j-1]
            else: i += 1
        if j == M:
            F.append(i-j+1)
            result += 1
            j = lps[j-1]
T = input()
P = input()
result = 0
F = []
KMP(P, T)
print(result)
print(*F)