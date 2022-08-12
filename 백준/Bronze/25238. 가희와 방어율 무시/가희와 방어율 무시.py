a,b = map(int,input().split())
print(0 if (a -  (b/100 * a)) >= 100.0 else 1)