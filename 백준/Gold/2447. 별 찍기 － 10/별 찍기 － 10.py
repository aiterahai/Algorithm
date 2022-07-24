def append_star(LEN):
    if LEN == 1: return '*'
    L, stars = [], append_star(LEN // 3)
    for S in stars: L.append(S * 3)
    for S in stars: L.append(S + ' ' * (LEN // 3) + S)
    for S in stars: L.append(S * 3)
    return L
print('\n'.join(append_star(int(input()))))