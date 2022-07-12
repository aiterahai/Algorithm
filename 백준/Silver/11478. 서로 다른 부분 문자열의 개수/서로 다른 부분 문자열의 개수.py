N = input()
S = set()
for i in range(1, len(N) + 1):
    j = 0
    while j + i <= len(N):
        try:
            S.add(N[j:j + i])
            j += 1
        except: break
print(len(S))