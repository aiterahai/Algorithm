T, S = input(), input()
while T != S:
    if len(T) == len(S): print(0); exit(0)
    if S[-1] == "A": S = S[:-1]
    else: S = (S[::-1])[1:]
print(1)