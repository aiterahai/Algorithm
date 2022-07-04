from sys import stdin

while True:
    number = 1
    length = 1
    try: T = int(stdin.readline())
    except: break
    while number % T != 0:
        number += 10 ** length
        length += 1
    print(length)