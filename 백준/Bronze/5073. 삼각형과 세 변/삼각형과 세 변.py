from sys import stdin

while True:
    x, y, z = sorted(map(int, stdin.readline().split()), reverse=True)
    if not(x or y or z): break
    if y + z <= x:
        print("Invalid")
        continue
    if x == y == z:
        print("Equilateral")
        continue
    elif x != y != z:
        print("Scalene")
        continue
    else:
        print("Isosceles")