S = input()
for i in sorted([S[i:] for i in range(len(S))]): print(i)