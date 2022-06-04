from sys import stdin
n, m = map(int, stdin.readline().split())
arr = [stdin.readline()[:-1] for i in range(n)]
illustrated_book_ch = dict(zip(arr, range(1, n+1)))
illustrated_book_num = dict(zip(range(1, n+1), arr))
for i in range(m):
    temp = stdin.readline()[:-1]
    if temp.isdigit():
        print(illustrated_book_num[int(temp)])
    else:
        print(illustrated_book_ch[temp])