from sys import stdin

N, M = map(int, stdin.readline().split())
n_set, m_set = set(), set()
for i in range(N): n_set.add(str(stdin.readline().split()))
for i in range(M): m_set.add(str(stdin.readline().split()))
print(len(n_set & m_set))
for i in sorted(n_set & m_set): print(i[2:-2])