from collections import Counter

S = input()
result = [int(S[0])]
for i in S[1:]:
    if int(i) != result[-1]: result.append(int(i))
result = Counter(result)
print(min(result.values()) if (len(result.keys()) == 2) else "0")