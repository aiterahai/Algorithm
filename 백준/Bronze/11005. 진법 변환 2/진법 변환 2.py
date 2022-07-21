def convert_notation(n, base):
    T = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    q, r = divmod(n, base)
    return convert_notation(q, base) + T[r] if q else T[r]
N, B = map(int, input().split())
print(convert_notation(N, B))