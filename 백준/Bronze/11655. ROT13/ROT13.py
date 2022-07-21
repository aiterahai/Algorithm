arr=input()
for i in arr:
    if i.islower(): print(chr(97+(ord(i)+13-97)%26), end='')
    elif i.isupper(): print(chr(65+(ord(i)+13-65)%26), end='')
    else: print(i, end='')