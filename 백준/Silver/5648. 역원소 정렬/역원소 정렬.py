from sys import stdin
print(*sorted([int(i[::-1]) for i in stdin.read().split()[1:]]), sep="\n")