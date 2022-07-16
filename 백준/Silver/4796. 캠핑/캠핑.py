from sys import stdin

cnt = 1
while True:
    L, P, V = map(int, stdin.readline().split())
    if not L and not P and not V: break
    print(f"Case {cnt}: {L * (V // P) + V % P}" if V % P <= L else f"Case {cnt}: {L * (V // P) + L}")
    cnt += 1