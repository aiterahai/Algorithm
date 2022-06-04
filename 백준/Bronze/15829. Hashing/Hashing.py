n = int(input())
arr = input()
hash_value = 0
for i in range(n):
    hash_value += (ord(arr[i])-96)*(31**i)
    hash_value %= 1234567891
print(hash_value)