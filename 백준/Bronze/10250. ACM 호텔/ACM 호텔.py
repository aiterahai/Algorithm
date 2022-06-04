for i in range(int(input())):
    h, w, n = map(int, input().split())
    print(((n-1)%h)+1, end="")
    if((n-1)//h <= 8): print("0", end="")
    print(((n-1)//h) + 1)